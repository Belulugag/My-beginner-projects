import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QButtonGroup
from PyQt6.QtCore import Qt

class XO(QWidget):
    def __init__(self):
        super().__init__()
        # Инициализация атрибута self.buttons перед его использованием
        self.buttons = {} # Создаем пустой словарь для кнопок
        self.initUI()
        self.setGeometry(500, 500, 300, 400)
        self.setWindowTitle("Крестики-нолики")

        self.current_player = "X"
        self.game_over = False

    def initUI(self):
        main_layout = QVBoxLayout()

        player_select_layout = QHBoxLayout()
        self.radiobX = QRadioButton("X")
        self.radiobO = QRadioButton("O")
        self.radiobX.setChecked(True)
        self.radiobX.toggled.connect(self.change_player)
        self.radiobO.toggled.connect(self.change_player)
        player_select_layout.addWidget(QLabel("Ходит:"))
        player_select_layout.addWidget(self.radiobX)
        player_select_layout.addWidget(self.radiobO)
        player_select_layout.addStretch(1)

        board_layout = QVBoxLayout()
        buttons_layout_config = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]

        for row_buttons_config in buttons_layout_config:
            row_layout = QHBoxLayout()
            for button_id in row_buttons_config:
                btn = QPushButton("")
                btn.setFixedSize(80, 80)
                btn.clicked.connect(lambda checked, btn_id=button_id: self.button_click(btn_id))
                # Здесь кнопка успешно добавляется в self.buttons
                self.buttons[button_id] = btn
                row_layout.addWidget(btn)
            board_layout.addLayout(row_layout)

        self.new_game_button = QPushButton("Новая игра")
        self.new_game_button.clicked.connect(self.reset_game)

        self.status_label = QLabel("Ходит: X")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_layout.addLayout(player_select_layout)
        main_layout.addLayout(board_layout)
        main_layout.addWidget(self.new_game_button)
        main_layout.addWidget(self.status_label)

        self.setLayout(main_layout)

    def change_player(self):
        if self.radiobX.isChecked():
            self.current_player = "X"
        else:
            self.current_player = "O"
        self.update_status()

    def button_click(self, button_id):
        if self.game_over:
            return

        btn = self.buttons[button_id]
        if btn.text() == "":
            btn.setText(self.current_player)
            btn.setEnabled(False)

            if self.check_win():
                self.status_label.setText(f"Игрок {self.current_player} выиграл!")
                self.game_over = True
                self.disable_all_buttons()
            elif self.check_draw():
                self.status_label.setText("Ничья!")
                self.game_over = True
            else:
                self.switch_player()
                self.update_status()

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
            self.radiobX.setChecked(False)
            self.radiobO.setChecked(True)
        else:
            self.current_player = "X"
            self.radiobO.setChecked(False)
            self.radiobX.setChecked(True)

    def update_status(self):
        if not self.game_over:
            self.status_label.setText(f"Ходит: {self.current_player}")

    def check_win(self):
        win_conditions = [
            ["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"],
            ["1", "4", "7"], ["2", "5", "8"], ["3", "6", "9"],
            ["1", "5", "9"], ["3", "5", "7"]
        ]
        for condition in win_conditions:
            if (self.buttons[condition[0]].text() == self.current_player and
                self.buttons[condition[1]].text() == self.current_player and
                self.buttons[condition[2]].text() == self.current_player):
                return True
        return False

    def check_draw(self):
        for btn in self.buttons.values():
            if btn.text() == "":
                return False
        return True

    def reset_game(self):
        self.game_over = False
        for btn in self.buttons.values():
            btn.setText("")
            btn.setEnabled(True)
        self.current_player = "X"
        self.radiobX.setChecked(True)
        self.radiobO.setChecked(False)
        self.update_status()

    def disable_all_buttons(self):
        for btn in self.buttons.values():
            btn.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = XO()
    ex.show()
    sys.exit(app.exec())

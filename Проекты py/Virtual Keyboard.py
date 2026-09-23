import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLineEdit
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class VirtualKeyboard(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Виртуальная клавиатура")

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.input_field = QLineEdit()
        self.input_field.setFixedHeight(60)
        font = QFont()
        font.setPointSize(20)
        self.input_field.setFont(font)
        self.input_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Поле ввода занимает одну строку и все 10 колонок в сетке
        self.layout.addWidget(self.input_field, 0, 0, 1, 10)

        buttons_layout = [
            ["~", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-"],
            ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L", ":"],
            ["Z", "X", "C", "V", "B", "N", "M", "<", ">", "?"],
            ["Space", "Backspace"] # Отдельный ряд для специальных кнопок
        ]

        row_start_index = 1

        for row_idx, row_buttons in enumerate(buttons_layout):
            current_col_idx = 0 
            for button_text in row_buttons:
                btn = QPushButton(button_text)
                btn.setFixedSize(70, 50)
                button_font = QFont()
                button_font.setPointSize(14)
                btn.setFont(button_font)
                btn.clicked.connect(lambda _, text=button_text: self.on_button_click(text))

                if button_text == "Space":
                    # Кнопка "Space" занимает 6 колонок
                    self.layout.addWidget(btn, row_start_index + row_idx, current_col_idx, 1, 6)
                    current_col_idx += 6 
                elif button_text == "Backspace":
                    # Кнопка "Backspace" занимает 4 колонки
                    self.layout.addWidget(btn, row_start_index + row_idx, current_col_idx, 1, 4)
                    current_col_idx += 4
                else:
                    self.layout.addWidget(btn, row_start_index + row_idx, current_col_idx, 1, 1)
                    current_col_idx += 1

    def on_button_click(self, text):
        if text == "Space":
            # Вставляем пробел в текущую позицию курсора
            self.input_field.insert(" ")
        elif text == "Backspace":
            cursor_pos = self.input_field.cursorPosition()
            if cursor_pos > 0:
                self.input_field.setCursorPosition(cursor_pos - 1)
                self.input_field.del_()
        elif text == "<":
            cursor_pos = self.input_field.cursorPosition()
            if cursor_pos > 0:
                self.input_field.setCursorPosition(cursor_pos - 1)
        elif text == ">":
            cursor_pos = self.input_field.cursorPosition()
            if cursor_pos < len(self.input_field.text()):
                self.input_field.setCursorPosition(cursor_pos + 1)
        else:
            self.input_field.insert(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    keyboard = VirtualKeyboard()
    keyboard.show()
    sys.exit(app.exec())

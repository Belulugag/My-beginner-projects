import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLCDNumber, QCheckBox, QVBoxLayout, QHBoxLayout, QListWidget
from PyQt6.QtCore import Qt

class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.current_song_index = 0
        self.is_playing = False
        self.songs = ["Song 1", "Song 2", "Song 3", "Song 4"]
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 400, 400, 400)
        self.setWindowTitle("Music Player")

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        top_layout = QHBoxLayout()
        self.song_title_label = QLabel("No song selected", self)
        self.song_title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        top_layout.addWidget(self.song_title_label)

        self.playback_status_label = QLabel("Playback stopped", self)
        self.playback_status_label.setStyleSheet("font-size: 14px;")
        top_layout.addWidget(self.playback_status_label)
        main_layout.addLayout(top_layout)

        center_layout = QVBoxLayout()

        self.playlist_widget = QListWidget()
        self.playlist_widget.addItems(self.songs)
        self.playlist_widget.itemClicked.connect(self.select_song_from_list)
        center_layout.addWidget(self.playlist_widget)

        self.song_number_lcd = QLCDNumber(self)
        self.song_number_lcd.display(self.current_song_index + 1)
        center_layout.addWidget(self.song_number_lcd, alignment=Qt.AlignmentFlag.AlignCenter)

        self.play_pause_button = QPushButton("Play", self)
        self.play_pause_button.setFixedSize(150, 50)
        self.play_pause_button.clicked.connect(self.toggle_playback)
        center_layout.addWidget(self.play_pause_button, alignment=Qt.AlignmentFlag.AlignCenter)

        nav_buttons_layout = QHBoxLayout()
        self.prev_button = QPushButton("Previous", self)
        self.prev_button.clicked.connect(self.previous_song)
        nav_buttons_layout.addWidget(self.prev_button)

        self.next_button = QPushButton("Next", self)
        self.next_button.clicked.connect(self.next_song)
        nav_buttons_layout.addWidget(self.next_button)
        center_layout.addLayout(nav_buttons_layout)
        main_layout.addLayout(center_layout)

        style_layout = QHBoxLayout()
        style_label = QLabel("Music Styles:", self)
        style_layout.addWidget(style_label)

        self.blues_checkbox = QCheckBox("Blues", self)
        self.blues_checkbox.stateChanged.connect(self.on_style_changed)
        style_layout.addWidget(self.blues_checkbox)

        self.jazz_checkbox = QCheckBox("Jazz", self)
        self.jazz_checkbox.stateChanged.connect(self.on_style_changed)
        style_layout.addWidget(self.jazz_checkbox)

        self.rock_checkbox = QCheckBox("Rock", self)
        self.rock_checkbox.stateChanged.connect(self.on_style_changed)
        style_layout.addWidget(self.rock_checkbox)
        main_layout.addLayout(style_layout)

        self.update_display()

    def toggle_playback(self):
        self.is_playing = not self.is_playing
        self.playback_status_label.setText("Playing" if self.is_playing else "Playback stopped")
        self.play_pause_button.setText("Pause" if self.is_playing else "Play")
        self.update_display()

    def next_song(self):
        if self.songs:
            self.current_song_index = (self.current_song_index + 1) % len(self.songs)
            self.playlist_widget.setCurrentRow(self.current_song_index)
            self.update_display()

    def previous_song(self):
        if self.songs:
            self.current_song_index = (self.current_song_index - 1 + len(self.songs)) % len(self.songs)
            self.playlist_widget.setCurrentRow(self.current_song_index)
            self.update_display()

    def select_song_from_list(self, item):
        self.current_song_index = self.playlist_widget.currentRow()
        self.update_display()

    def on_style_changed(self, state):
        checkbox = self.sender()
        style_name = checkbox.text()
        if state == Qt.CheckState.Checked.value:
            print(f"Style '{style_name}' selected.")
        else:
            print(f"Style '{style_name}' deselected.")

    def update_display(self):
        self.song_title_label.setText(self.songs[self.current_song_index] if self.songs else "No songs available")
        self.song_number_lcd.display(self.current_song_index + 1)
        self.playback_status_label.setText("Playing" if self.is_playing else "Playback stopped")
        self.play_pause_button.setText("Pause" if self.is_playing else "Play")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MusicPlayer()
    ex.show()
    sys.exit(app.exec())

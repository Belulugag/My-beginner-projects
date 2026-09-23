import sys
from PyQt6.QtWidgets import QApplication,QWidget

class widget(QWidget):
    def __init__(self):
        super().__init__()

    def initUI(self):
        self.setGeometry(700,400,250,500)
        self.setWindowTitle("PyQT6 1")
        btn = QPushButton("Привет,я кнопка и я прийду к тебе в 3 часа ночи")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ge = widget()
    ge.show()
    sys.exit(app.exec())
    btn.

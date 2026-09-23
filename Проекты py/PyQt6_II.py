import sys
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QLCDNumber
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def inirUI(self):
        self.setGeometry(700,400,250,250)
        self.setWindowTitle("PyQt II")
        self.lb01 = QLabel("0",self)
        self.lb01.move(125,50)
        self.btn  = QPushButton("Ещё приходов к тебе домой в 3 часа ночи",self)
        delf.btn.resize(150,50)
        self.btn.move(50,100)
        self.btn.clicked.connect(self.countPrihodiuy)

    def countPrihodiuy(self):
        self.lb01.setText(str(int(self.lb01.text())+1))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

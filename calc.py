import sys
from PyQt5.QtWidgets import QApplication, QWidget, QStyleFactory
from PyQt5.uic import loadUi

from qt_material import apply_stylesheet, list_themes

class Main(QWidget):
    def __init__(self) -> None:
        QWidget.__init__(self)
        loadUi('static/calculator.ui', self)

        # apply_stylesheet(self, theme="dark_red.xml")
        


        self.buttonhandle()
        self.setWindowTitle('Delight Calc')
        self.show()

    def buttonhandle(self):
        self.btn1.clicked.connect(self.addone)
        self.btn2.clicked.connect(self.addtwo)
        self.btn3.clicked.connect(self.addthree)
        self.btn4.clicked.connect(lambda: self.addNum(4))
        self.btn5.clicked.connect(lambda: self.addNum(5))
        self.btn6.clicked.connect(lambda: self.addNum(6))

    def addNum(self, number):
        value = self.lblInput.text()
        if value == '0':
            self.lblInput.setText(str(number))
        else:
            self.lblInput.setText(value+str(number))


    def addone(self):
        self.lblInput.setText('1')

    def addtwo(self):
        self.lblInput.setText('2')

    def addthree(self):
        self.lblInput.setText('3')


app = QApplication(sys.argv)
app.setStyle('fusion')
window = Main()
sys.exit(app.exec_())
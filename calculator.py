import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStyleFactory
from PyQt5.uic import loadUi


class Calculator(QWidget):
    

    def __init__(self) -> None:
        QWidget.__init__(self)
        loadUi('static/calculator.ui', self)

        self.initial_value = '0' # Global variable for input

        self.buttonhandle()
        self.setWindowTitle('calculator')
        self.show()

    def buttonhandle(self):
        self.btn0.clicked.connect(lambda: self.addNum(0))
        self.btn1.clicked.connect(lambda: self.addNum(1))
        self.btn2.clicked.connect(lambda: self.addNum(2))
        self.btn3.clicked.connect(lambda: self.addNum(3))
        self.btn7.clicked.connect(lambda: self.addNum(7))
        self.btn8.clicked.connect(lambda: self.addNum(8))
        self.btn9.clicked.connect(lambda: self.addNum(9))
        self.btn4.clicked.connect(lambda: self.addNum(4))
        self.btn5.clicked.connect(lambda: self.addNum(5))
        self.btn6.clicked.connect(lambda: self.addNum(6))
        self.btn_decimal.clicked.connect(lambda: self.addNum('.'))

        # Working with Signs
        self.btn_plus.clicked.connect(lambda: self.calculate('+'))
        self.btn_minus.clicked.connect(lambda: self.calculate('-'))
        self.btn_multiply.clicked.connect(lambda: self.calculate('x'))
        self.btn_division.clicked.connect(lambda: self.calculate('/'))
        self.btn_equal.clicked.connect(lambda: self.calculate('='))

    def calculate(self, sign):
        value = self.lblInput.text()
        holder = self.lblHolder.text()
        if sign != "=":
            if sign == "x":
                sign = '*'
            self.lblHolder.setText(holder + value + " " + sign)
            self.lblInput.setText('0')
        else:
            holder += value
            self.lblInput.setText(str(eval(holder)))
            self.lblHolder.setText('')
            self.initial_value = '0'


    def addNum(self, number):
        value = self.lblInput.text()
        value = value.replace(',', '')
        if len(value) <= 15:
            if self.initial_value == '0':
                print(self.initial_value)
                self.lblInput.setText(str(number))
                self.initial_value = str(number)
            else:
                try:
                    if number == '.':
                        if not number in value:
                            value += str(number)
                            self.lblInput.setText("{:,}".format(int(value)))
                    else:
                        value += str(number)
                        self.lblInput.setText("{:,}".format(int(value)))
                except Exception as err:
                    print("Error Msg: ", err)

    def addone(self):
        self.lblInput.setText('1')


app = QApplication(sys.argv)
app.setStyle('fusion')
print(QStyleFactory.keys())
delight = Calculator()
sys.exit(app.exec_())

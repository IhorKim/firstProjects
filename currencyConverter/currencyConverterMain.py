# in terminal type: pip install PyQt5
# in terminal type: pip install PyQt5Designer
# in terminal type: pip install CurrencyConverter
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from currencyConverter import Ui_MainWindow  # currencyConverter.py
from currency_converter import CurrencyConverter


class Money(QtWidgets.QMainWindow):  # our main class
    def __init__(self):
        super(Money, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):  # changing window title
        self.setWindowTitle("Currency Converter")
        self.setWindowIcon(QIcon("dol.jpg"))  # icon before window title

        self.ui.input_currency.setPlaceholderText("From Currency:")  # filling empty fields
        self.ui.input_amount.setPlaceholderText("I have:")
        self.ui.output_currency.setPlaceholderText("To Currency:")
        self.ui.output_amount.setPlaceholderText("I will receive:")

        self.ui.pushButton.clicked.connect(self.converter)

    def converter(self):
        c = CurrencyConverter()  # using CurrencyConverter module
        input_currency = self.ui.input_currency.text()
        input_amount = int(self.ui.input_amount.text())
        output_currency = self.ui.output_currency.text()

        output_amount = round(c.convert(input_amount, "%s" % input_currency, "%s" % output_currency), 2)  # formatting strings for CurrencyConverter

        self.ui.output_amount.setText(str(output_amount))  # placing the result


app = QtWidgets.QApplication([])
application = Money()
application.show()

sys.exit(app.exec())

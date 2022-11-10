from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setStyleSheet("background-color: #223843;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 20, 550, 300))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("QPlainTextEdit{\n"
"background-color: #D77A61;\n"
"border: 5px solid \"red\";\n"
"color: \"white\";\n"
"}")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 350, 550, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"background-color: #D8B4A0;\n"
"border: 5px solid \"red\";\n"
"color: \"black\";\n"
"}")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 430, 550, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: #DBD3D8;\n"
"border: 5px solid \"red\";\n"
"color: \"black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: \"brown\";\n"
"border: 5px solid \"red\";\n"
"color: \"black\";\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #DBD3D8;\n"
"border: 5px solid \"white\";\n"
"color: \"black\";\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 510, 550, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: #EFF1F3;\n"
"border: 5px solid \"red\";\n"
"color: \"black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: \"brown\";\n"
"border: 5px solid \"red\";\n"
"color: \"black\";\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #DBD3D8;\n"
"border: 5px solid \"white\";\n"
"color: \"black\";\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Choose a folder to save"))
        self.pushButton_2.setText(_translate("MainWindow", "Download Video"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

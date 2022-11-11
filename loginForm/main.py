"""
in terminal type: pip install PyQt5
in terminal type: pip install PyQt5Designer
in terminal type: pip install db-sqlite3
"""
import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from form import Ui_MainWindow

db = sqlite3.connect("mydatabase.db")  # creating database
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(  
    login TEXT,
    password TEXT
)""")  # creating database table
db.commit()  # confirm creating table

for i in cursor.execute("SELECT * FROM users"):  # reading data in table
    print(i)


class RegistrationForm(QtWidgets.QMainWindow):  # our main class
    def __init__(self):
        super(RegistrationForm, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Login")  # changing window title
        self.setWindowIcon(QIcon("key.png"))  # icon before window title
        self.ui.lineEdit.setPlaceholderText("Enter your Login here...")  # filling empty fields
        self.ui.lineEdit_2.setPlaceholderText("Enter your password here...")
        self.ui.pushButton.setText("Sign in")
        self.ui.pushButton_2.setText("Registration")

        self.ui.pushButton.pressed.connect(self.reg)
        self.ui.pushButton_2.pressed.connect(self.login)

    def reg(self):  # checking data
        user_login = self.lineEdit.text()
        user_password = self.lineEdit_2.text()

        if len(user_login) == 0:
            return

        if len(user_password) == 0:
            return

        cursor.execute(f"SELECT login FROM users WHERE login='{user_login}'")  # interaction with database
        if cursor.fetchone() is None:
            cursor.execute(f"INSERT INTO users VALUES ('{user_login}', '{user_password}')")
            self.ui.label_2.setText(f"Account {user_login} registered successfully!")
            db.commit()
        else:
            self.ui.label_2.setText("Such login already exists!")

    def login(self):
        self.login = Login()
        self.login.show()
        self.hide()


class Login(QtWidgets.QMainWindow):

    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon("key.png"))
        self.ui.lineEdit.setPlaceholderText("Enter your Login here...")
        self.ui.lineEdit_2.setPlaceholderText("Enter your password here...")
        self.ui.pushButton.setText("Sign in")
        self.ui.pushButton_2.setText("Registration")

        self.ui.pushButton.pressed.connect(self.login)
        self.ui.pushButton_2.pressed.connect(self.reg)

    def reg(self):
        self.reg = RegistrationForm()
        self.reg.show()
        self.hide()

    def login(self):
        user_login = self.lineEdit.text()
        user_password = self.lineEdit_2.text()

        if len(user_login) == 0:
            return

        if len(user_password) == 0:
            return

        cursor.execute(f"SELECT password FROM users WHERE login='{user_login}'")  # checking data
        check_password = cursor.fetchall()

        cursor.execute(f"SELECT login FROM users WHERE login='{user_login}'")
        check_login = cursor.fetchall()

        if check_password[0][0] == user_password and check_login[0][0] == user_login:
            self.ui.label_2.setText("Authorization successful!")
        else:
            self.ui.label_2.setText("Error Authorization!")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Login()
    application.show()

    sys.exit(app.exec())




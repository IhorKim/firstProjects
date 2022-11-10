"""
in terminal type: pip install PyQt5
in terminal type: pip install PyQt5Designer
in terminal type: pip install youtube_dl
"""
import os
import sys
import youtube_dl
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtWidgets
from qw import Ui_MainWindow


class Main(QtWidgets.QMainWindow):  # our main class
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.download_folder = None
        self.ui.pushButton.clicked.connect(self.get_folder)  # action for pushButton
        self.ui.pushButton_2.clicked.connect(self.start)  # action for pushButton_2
        self.mycord = Download()  # main operation
        self.mycord.mysignal.connect(self.handler)

        self.init_UI()

    def init_UI(self):  # changing window title
        self.setWindowTitle("Youtube video Downloader")
        self.setWindowIcon(QIcon("play.png"))  # icon before window title
        self.ui.plainTextEdit.setPlaceholderText("Process information")  # filling empty fields
        self.ui.lineEdit.setPlaceholderText("https://youtube.com/...")

    def start(self):  # checking all necessary data
        if len(self.ui.lineEdit.text()) > 5:
            if self.download_folder != None:
                link = self.ui.lineEdit.text()
                self.mycord.init_args(link)
                self.mycord.start()
                self.locker(True)
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "You have not choose a folder!")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "No video URL!")

    def get_folder(self):
        self.download_folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Please choose a folder to save file")
        os.chdir(self.download_folder)

    def handler(self, value):  # reflect progress steps
        if value == "finish":
            self.locker(False)
        else:
            self.ui.plainTextEdit.appendPlainText(value)

    def locker(self, lock_value):  # lock buttons when the file is downloading
        base = [self.ui.pushButton, self.ui.pushButton_2]

        for item in base:
            item.setDisabled(lock_value)


class Download(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Download, self).__init__()
        self.url = None

    def run(self):
        self.mysignal.emit("Downloading file...")

        with youtube_dl.YoutubeDL({}) as ydl:
            ydl.download([self.url])

        self.mysignal.emit("Downloading is done!")
        self.mysignal.emit("Finish!")

    def init_args(self, url):
        self.url = url


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Main()
    application.show()

    sys.exit(app.exec())

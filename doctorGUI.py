import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QDialog, QVBoxLayout, QWidget, QLabel, QLineEdit, \
    QFormLayout, QAction, QToolButton
import patientInfo
import patientInfo as pI


class App(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('layout/receiver_log_in.ui', self)
        self.setWindowTitle("First app")
        self.username = self.findChild(QLineEdit, 'username')
        self.password = self.findChild(QLineEdit, 'password')
        self.password.setEchoMode(QLineEdit.Password)
        self.loginButton = self.findChild(QPushButton, 'loginButton')
        self.loginButton.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        try:
            if (self.username.text() == "test") and (self.password.text() == "text"):
                print("Login")
                self.patientInfo = pI.patientInfo()
                self.patientInfo.show()
        except Exception as e:
            print(e)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
window.show()
sys.exit(app.exec_())

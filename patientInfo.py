import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QDialog, QVBoxLayout, QWidget, QLabel, QLineEdit, \
    QFormLayout, QAction, QToolButton

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('layout/receiver_select_patient.ui', self)
        self.setWindowTitle("First app")
        self.dropdown = self.find
def start():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    start()
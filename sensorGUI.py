import sys
import threading

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel
import main as sM
import sensor.utils as ut


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('layout/simulate_sensor.ui', self)
        self.setWindowTitle("First app")
        self.bloodID = self.findChild(QLabel, 'bloodID')
        self.bloodValue = self.findChild(QLabel, 'bloodValue')
        self.cholID = self.findChild(QLabel, 'cholID')
        self.cholValue = self.findChild(QLabel, 'cholValue')
        self.heartID = self.findChild(QLabel, 'heartID')
        self.heartValue = self.findChild(QLabel, 'heartValue')
        self.sugarID =  self.findChild(QLabel, 'sugarID')
        self.sugarValue = self.findChild(QLabel, 'sugarValue')
        self.tempID = self.findChild(QLabel, 'tempID')
        self.tempValue = self.findChild(QLabel, 'tempValue')
        self.startButton = self.findChild(QPushButton, 'startButton')
        self.mainThreadID = ""
        self.run = False;
        self.startButton.clicked.connect(self.buttonClicked)
        self.setSensorsID()

    def setSensorsID(self):
        self.bloodID.setText(ut.bloodID)
        self.cholID.setText(ut.cholID)
        self.heartID.setText(ut.heartID)
        self.sugarID.setText(ut.sugarID)
        self.tempID.setText(ut.tempID)

    def buttonClicked(self):
        try:
            if not self.run:
                self.run = True
                self.printInfo()
                self.startButton.setText("Stop")
            else:
                self.run = False
                self.stopSimulate()
                self.startButton.setText("Start")
        except Exception as e:
            print(e)

    def updateValue(self):
        while True:
                self.sugarValue.setText(str(ut.sugar))
                self.heartValue.setText(str(ut.heart))
                self.tempValue.setText(str(ut.temperature))
                self.cholValue.setText(str(ut.cholesterol))
                self.bloodValue.setText(str(ut.bloodHigh) + "|" + str(ut.bloodLow))

    def startSimulate(self):
        sM.start()

    def stopSimulate(self):
        sM.stop()

    def printInfo(self):
        try:
            t = threading.Thread(target=self.startSimulate, daemon=True)
            info = threading.Thread(target=self.updateValue, daemon=True)
            t.start()
            info.start()

        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
window.show()
sys.exit(app.exec_())

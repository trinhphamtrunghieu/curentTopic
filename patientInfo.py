import sys
import threading
import time

from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QDialog, QVBoxLayout, QWidget, QLabel, QLineEdit, \
    QFormLayout, QAction, QToolButton, QComboBox, QGridLayout
import receiver.doctorMain as dt
import receiver.utils as ut


def checkTime():
    return 0 < ut.t < 4;


class patientInfo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        try:
            uic.loadUi('layout/receiver_select_patient.ui', self)
            self.setWindowTitle("First app")
            self.dropdown = self.findChild(QComboBox, 'selectPatientComboBox')
            self.dropdown.addItem("--")
            self.dropdown.addItem("hieu")
            self.dropdown.currentIndexChanged.connect(self.printInfo)
            self.bloodValue = self.findChild(QLabel, 'bloodValue')
            self.heartValue = self.findChild(QLabel, 'heartValue')
            self.sugarValue = self.findChild(QLabel, 'sugarValue')
            self.tempValue = self.findChild(QLabel, 'tempValue')
            self.cholValue = self.findChild(QLabel, 'cholValue')
        except Exception as e:
            print(e.with_traceback())

    def startListen(self):
        dt.start()

    def updateValue(self):
        while True:
            if (ut.bloodHigh != ""):
                print("Blood " + str(ut.bloodHigh) + "|" + str(ut.bloodLow))
                print("Cholesterol " + str(ut.cholesterol))
                print("Heart beat " + str(ut.heart))
                print("Sugar " + str(ut.sugar))
                print("Temperature " + str(ut.temperature))
                self.checkAlarm()
                self.updateGUI()
            time.sleep(2)

    def updateGUI(self):
        self.cholValue.setText(str(ut.cholesterol))
        self.bloodValue.setText(str(ut.bloodHigh) + "|" + str(ut.bloodLow))
        self.tempValue.setText(str(ut.temperature) + "{}\u00b0C".format(""))
        self.heartValue.setText(str(ut.heart))
        self.sugarValue.setText(str(ut.sugar))

    def checkAlarm(self):
        self.checkBloodAlarm()
        self.checkTempAlarm()
        self.checkCholAlarm()
        self.checkHeartAlarm()
        self.checkSugarAlarm()

    def checkBloodAlarm(self):
        pal = self.bloodValue.palette()
        try:
            if ut.bloodHigh < 90 and ut.bloodLow < 60:
                #            self.bloodValue.setStyleSheet("{color:ff0000")
                pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                self.bloodValue.setPalette(pal)
            elif (120 < ut.bloodHigh < 140) and (80 < ut.bloodLow < 90):
                pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                self.bloodValue.setPalette(pal)
            elif (ut.bloodHigh >= 140) and (ut.bloodLow >= 90):
                pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                self.bloodValue.setPalette(pal)
            else:
                pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"));
                self.bloodValue.setPalette(pal)
        except Exception as e:
            print(e)

    def checkTempAlarm(self):
        pal = self.tempValue.palette()
        if ut.temperature < 20 :
            pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
            self.tempValue.setPalette(pal)
        elif ut.temperature > 38 :
            pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
            self.tempValue.setPalette(pal)
        else:
            pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"));
            self.tempValue.setPalette(pal)

    def checkCholAlarm(self):
        pal = self.cholValue.palette()
        if 200 < ut.cholesterol:
            pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
            self.cholValue.setPalette(pal)
        else :
            pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"));
            self.cholValue.setPalette(pal)

    def checkHeartAlarm(self):
        pal = self.heartValue.palette()
        if ut.sex=='M':
            if 6 <= ut.age <= 11:
                if ut.heart < 88:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                    self.heartValue.setPalette(pal)
                elif ut.heart > 109:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                    self.heartValue.setPalette(pal)
                else:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"));
                    self.heartValue.setPalette(pal)
            elif 12 <= ut.age <= 19:
                if ut.heart < 86:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                    self.heartValue.setPalette(pal)
                elif ut.heart > 108:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                    self.heartValue.setPalette(pal)
                else:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"));
                    self.heartValue.setPalette(pal)
            if 20 <= ut.age <= 39:
                if ut.heart < 82:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                    self.heartValue.setPalette(pal)
                elif ut.heart > 86:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                    self.heartValue.setPalette(pal)
                else:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"));
                    self.heartValue.setPalette(pal)
            elif 40 <= ut.age <= 59:
                if ut.heart < 81:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                    self.heartValue.setPalette(pal)
                elif ut.heart > 91:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                    self.heartValue.setPalette(pal)
                else:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"));
                    self.heartValue.setPalette(pal)
            elif 60 <= ut.age <= 79:
                if ut.heart < 80:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                    self.heartValue.setPalette(pal)
                elif ut.heart > 92:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                    self.heartValue.setPalette(pal)
                else:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"));
                    self.heartValue.setPalette(pal)
            else:
                if ut.heart < 85:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                    self.heartValue.setPalette(pal)
                elif ut.heart > 90:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                    self.heartValue.setPalette(pal)
                else:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"));
                    self.heartValue.setPalette(pal)
        elif ut.sex=='F':
            if 6 <= ut.age <= 11:
                if  ut.heart < 98:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                    self.heartValue.setPalette(pal)
                elif ut.heart > 110:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                    self.heartValue.setPalette(pal)
                else:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"));
                    self.heartValue.setPalette(pal)
            elif 12 <= ut.age <= 19:
                if ut.heart < 91:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                    self.heartValue.setPalette(pal)
                else:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"));
                    self.heartValue.setPalette(pal)
            if 20 <= ut.age <= 39:
                if ut.heart < 83:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                    self.heartValue.setPalette(pal)
                elif ut.heart > 88:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                    self.heartValue.setPalette(pal)
                else:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"));
                    self.heartValue.setPalette(pal)
            elif 40 <= ut.age <= 59:
                if ut.heart < 79:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                    self.heartValue.setPalette(pal)
                elif ut.heart > 86:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                    self.heartValue.setPalette(pal)
                else:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"));
                    self.heartValue.setPalette(pal)
            elif 60 <= ut.age <= 79:
                if ut.heart < 83:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                    self.heartValue.setPalette(pal)
                elif ut.heart > 88:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                    self.heartValue.setPalette(pal)
                else:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"));
                    self.heartValue.setPalette(pal)
            else:
                if ut.heart < 87:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                    self.heartValue.setPalette(pal)
                elif ut.heart > 90:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
                    self.heartValue.setPalette(pal)
                else:
                    pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"));
                    self.heartValue.setPalette(pal)

    def checkSugarAlarm(self):
        pal = self.sugarValue.palette()
        if ut.sugar > 130:
            pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
            self.sugarValue.setPalette(pal)
        elif ut.sugar < 54:
            pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"));
            self.sugarValue.setPalette(pal)
        else:
            pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"));
            self.sugarValue.setPalette(pal)

    def printInfo(self):
        try:
            t = threading.Thread(target=self.startListen, daemon=True)
            info = threading.Thread(target=self.updateValue, daemon=True)
            t.start()
            info.start()

        except Exception as e:
            print(e)

import random
import subprocess
import sys
import os

from PyQt5 import QtCore, QtGui, QtNetwork, QtWidgets

# Qt Windows
from Home import Ui_Home
from Dialog import Ui_Dialog

pi = "alex@raspberrypi"


def LEDOn():
    """ Turn on LED lights """
    SSH(pi, "~/Scripts/home_arduino.py on")


def LEDOff():
    """ Turn off LED lights """
    SSH(pi, "~/Scripts/home_arduino.py off")


def SSH(host, command):
    """ Send SSH command """
    subprocess.Popen("ssh {0} {1}".format(host, command), shell=True,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()


# Setup main window
App = QtWidgets.QApplication(sys.argv)
Qhome = QtWidgets.QMainWindow()
home = Ui_Home()
home.setupUi(Qhome)
Qdialog = QtWidgets.QDialog()
dialog = Ui_Dialog()
dialog.setupUi(Qdialog)

# Widget stuff
home.btnLEDOn.clicked.connect(LEDOn)
home.btnLEDOff.clicked.connect(LEDOff)
home.actionQuit.triggered.connect(App.exit)
home.actionAbout.triggered.connect(Qdialog.show)
dialog.lblMessage.setText("hdlgsj")
Qdialog.setWindowState()

# Load main window
Qhome.show()
Qhome.setWindowTitle("How are you today?")
sys.exit(App.exec_())

import random
import subprocess
import sys

from PyQt5 import QtCore, QtGui, QtNetwork, QtWidgets

# Qt Windows
from home import Ui_Home
from dialog import Ui_Dialog

pi = "alex@raspberrypi"


def LEDOn():
    SSH(pi, "~/Scripts/home_arduino.py on")


def LEDOff():
    SSH(pi, "~/Scripts/home_arduino.py off")


def SSH(host, command):
    subprocess.Popen("ssh {0} {1}".format(host, command), shell=True,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()


# Setup main window
App = QtWidgets.QApplication(sys.argv)
Home = QtWidgets.QMainWindow()
UI = Ui_Home()
UI.setupUi(Home)
Dialog = QtWidgets.QDialog()
dia = Ui_Dialog()
dia.setupUi(Dialog)

# Widget stuff
UI.btnLEDOn.clicked.connect(LEDOn)
UI.btnLEDOff.clicked.connect(LEDOff)
UI.actionQuit.triggered.connect(App.exit)
UI.actionAbout.triggered.connect(Dialog.show)

# Load main window
Home.show()
sys.exit(App.exec_())

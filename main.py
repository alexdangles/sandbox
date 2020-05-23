import random
import subprocess
import sys

from PyQt5 import QtCore, QtGui, QtNetwork, QtWidgets

from Dialog import Ui_Dialog
from MainWindow import Ui_MainWindow

pi = "alex@raspberrypi"


def LEDOn():
    SSH(pi, "~/Scripts/home_arduino.py on")


def LEDOff():
    SSH(pi, "~/Scripts/home_arduino.py off")


def SSH(host, command):
    subprocess.Popen("ssh {0} {1}".format(host, command), shell=True,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()


def GetRnd():
    ui.lcd1.display(random.random() * 6743.3363)


# Setup main window
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
Dialog = QtWidgets.QDialog()
di = Ui_Dialog()
di.setupUi(Dialog)
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

# Widget stuff
ui.btnOn.clicked.connect(LEDOn)
ui.btnOff.clicked.connect(LEDOff)
ui.actionQuit.triggered.connect(app.exit)
ui.dial.valueChanged.connect(GetRnd)
ui.label.setPixmap(QtGui.QPixmap(":/Main/My Car.jpg"))
ui.actionAbout.triggered.connect(Dialog.show)

# Load main window
MainWindow.show()
sys.exit(app.exec_())

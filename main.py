import os
import random
from subprocess import Popen, PIPE
import sys
from sys import stderr

from easysettings import load_json_settings
from PyQt5 import QtCore, QtGui, QtNetwork, QtWidgets

from dialog import Ui_Dialog
from home import Ui_Home

js = load_json_settings('settings.json')
js['pi'] = 'alex@pi'
pi = js['pi']


def LEDOn():
    """
    Turn on LED lights
    """
    print(Sh(pi, "~/scripts/home_arduino.py on"))
    js['led state'] = 'on'
    js.save()


def LEDOff():
    """
    Turn off LED lights
    """
    print(Sh(pi, "~/scripts/home_arduino.py off"))
    js['led state'] = 'off'
    js.save()


def Sh(host, command):
    """
    Send shell command
    """
    out, err = Popen(["ssh", "%s" % host, command],
                     stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate()
    if err == []:
        return err
    else:
        return out


# Setup main window
Qapp = QtWidgets.QApplication(sys.argv)
Qhome = QtWidgets.QMainWindow()
home = Ui_Home()
home.setupUi(Qhome)
Qdialog = QtWidgets.QDialog()
dialog = Ui_Dialog()
dialog.setupUi(Qdialog)

columns = ('skdjgl', 'sdag', 'hf', 'sdf')
rows = [100, 50]
data = [[66386, 174296,  75131, 577908],
        [58230, 381139,  78045,  99308],
        ]

columns1 = ('skdjgl', 'klsdjgklda', 'lagkjl')
rows1 = ['what']
data1 = [[66386, 174296,  75131, 577908,  32015]
         ]


# Widget stuff
home.btnLEDOn.clicked.connect(LEDOn)
home.btnLEDOff.clicked.connect(LEDOff)
home.actionQuit.triggered.connect(Qapp.exit)
home.actionAbout.triggered.connect(Qdialog.show)

# Load main window
Qhome.show()
Qhome.setWindowTitle("How are you today?")
sys.exit(Qapp.exec_())

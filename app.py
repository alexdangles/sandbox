import os
import random
import sys

from PyQt5 import QtCore, QtGui, QtNetwork, QtWidgets

import res_rc
from dialog import Ui_Dialog
from helper import *
from home import Ui_Home
from plotter import *

# Default settings
config['pi'] = 'alex@pi'
config['arduino'] = '~/scripts/home_arduino.py'

# Load saved settings (overrides defaults)
pi = config['pi']
arduino = config['arduino']


def SetIcon(icon):
    i = QtGui.QIcon()
    i.addPixmap(QtGui.QPixmap(':/main/icons/%s' % icon))
    return i


def Arduino(cmd):
    """Send command to Arduino.

    Keyword arguments:
    cmd: command to send
    """
    state = Ssh(pi, '%s %s' % (arduino, cmd))
    config[cmd] = state
    config.save()


def Plot():
    """Plot something.
    """
    fig = plt.figure(FigureClass=MyFigure)
    fig.suptitle('Main window title')
    ax = fig.subplots(1, 1)
    ax.set_title('X vs Y')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plot_histograms(ax, data, annotate=True)
    plt.show()


if __name__ == '__main__':
    # Init main window
    Qapp = QtWidgets.QApplication(sys.argv)
    Qhome = QtWidgets.QMainWindow()
    home = Ui_Home()
    home.setupUi(Qhome)

    # Init dialog window
    Qdialog = QtWidgets.QDialog()
    dialog = Ui_Dialog()
    dialog.setupUi(Qdialog)

    # Link widgets to funtions
    home.btnLED.clicked.connect(lambda: Arduino('leds'))
    home.btnLaser.clicked.connect(lambda: Arduino('laser'))
    home.actionQuit.triggered.connect(Qapp.exit)
    home.actionAbout.triggered.connect(Qdialog.show)
    home.actionSave.triggered.connect(Plot)

    # Load main window
    Qhome.setWindowTitle(config['app_name'])
    Qhome.show()
    Qapp.exec_()
    config.save(sort_keys=False)

import os
import random
import sys

from PyQt5 import QtCore, QtGui, QtNetwork, QtWidgets

import res_rc
from dialog import Ui_Dialog
from helper import *
from home import Ui_Home
from plotter import *

config['pi'] = 'alex@pi'

pi = config['pi']
arduino = config['arduino']


def SetNewIcon():
    i = QtGui.QIcon()
    i.addPixmap(QtGui.QPixmap(':/main/icons/alert round.png'))


def LED():
    """
    Control LED lights
    """
    res=Ssh(pi, '%s %s' % (arduino, 'leds')).decode().strip('\r\n')
    config['led_state'] = res
    config.save()

def Laser():
    """
    Control Laser
    """
    res=Ssh(pi, '%s %s' % (arduino, 'laser')).decode().strip('\r\n')
    config['laser_state'] = res
    config.save()

def Plot():
    """
    Plot something
    """
    fig = plt.figure(FigureClass=MyFigure)
    #fig.suptitle('Main window title')
    ax = fig.subplots(1, 1)
    ax.set_title('X vs Y')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plot_histograms(ax, data)


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
    home.btnLED.clicked.connect(lambda: LED())
    home.btnLaser.clicked.connect(lambda: Laser())
    home.actionQuit.triggered.connect(Qapp.exit)
    home.actionAbout.triggered.connect(Qdialog.show)
    home.actionOpen.triggered.connect(SetNewIcon)
    home.actionSave.triggered.connect(Plot)

# Load main window
    Qhome.setWindowTitle('Learning some Qt')
    Qhome.show()
    Qapp.exec_()
    config.save(sort_keys=False)

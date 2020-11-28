import os
import random
import sys
from helper import *
from PyQt5 import QtCore, QtGui, QtNetwork, QtWidgets

import res_rc
from dialog import Ui_Dialog
from home import Ui_Home
from plotter import *


config = load_json_settings('config.json')
config['pi'] = 'alex@pi'
pi = config['pi']


def SetNewIcon():
    i = QtGui.QIcon()
    i.addPixmap(QtGui.QPixmap(":/main/icons/alert round.png"))
    home.btnLEDOff.setIcon(i)


def LEDOn():
    """
    Turn on LED lights
    """
    print(Ssh(pi, "~/scripts/home_arduino.py on"))
    config['led state'] = 'on'


def LEDOff():
    """
    Turn off LED lights
    """
    print(Ssh(pi, "~/scripts/home_arduino.py off"))
    config['led state'] = 'off'


def Plot():
    """
    Plot something
    """
    fig = plt.figure(FigureClass=MyFigure)
    fig.suptitle('dink')
    ax = fig.subplots(1, 1)
    ax.set_title('bar graphs')
    plot_bar_graphs(ax, data)
    plt.show()


if __name__ == "__main__":
    # Setup main window
    Qapp = QtWidgets.QApplication(sys.argv)
    Qhome = QtWidgets.QMainWindow()
    home = Ui_Home()
    home.setupUi(Qhome)

    Qdialog = QtWidgets.QDialog()
    dialog = Ui_Dialog()
    dialog.setupUi(Qdialog)

    # Widget stuff
    home.btnLEDOn.clicked.connect(LEDOn)
    home.btnLEDOff.clicked.connect(LEDOff)
    home.actionQuit.triggered.connect(Qapp.exit)
    home.actionAbout.triggered.connect(Qdialog.show)
    home.actionOpen.triggered.connect(SetNewIcon)
    home.actionSave.triggered.connect(Plot)
    
    # Load main window
    Qhome.setWindowTitle("Learning some Qt")
    Qhome.show()
    Qapp.exec_()
    config.save(sort_keys=True)

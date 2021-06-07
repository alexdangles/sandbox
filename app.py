import os
import random
import sys
import sqlite3

from PyQt5 import QtGui, QtCore, QtWidgets, QtWebEngineWidgets

import res_rc
from dialog import Ui_Dialog
from helper import *
from home import Ui_Home
from plotter import *

# Default settings
config['pi'] = 'alex@pi'
config['arduino'] = '~/scripts/home_arduino.py'
log = Log(config['logfile'])

# Load saved settings (overrides defaults)
pi = config['pi']
arduino = config['arduino']


class Ui_Web(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):

        super(Ui_Web, self).__init__(*args, **kwargs)

        self.setWindowTitle('Mini Browser')
        self.setGeometry(5, 30, 1355, 730)

        self.browser = QtWebEngineWidgets.QWebEngineView()

        self.setCentralWidget(self.browser)

    def goTo(self, url):
        self.browser.load(QtCore.QUrl('http://' + url))


def SetIcon(icon):
    i = QtGui.QIcon()
    i.addPixmap(QtGui.QPixmap(':/main/icons/%s' % icon))
    return i


def Plot():
    """Plot something.
    """
    fig = plt.figure(FigureClass=MyFigure)
    ax = fig.subplots(1, 1)
    ax.set_title('X vs Y')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plot_scatter(ax, data)
    plt.show()


def Browser(url):
    web.goTo(url)
    web.show()


if __name__ == '__main__':
    # Init main window
    Qapp = QtWidgets.QApplication(sys.argv)
    Qhome = QtWidgets.QMainWindow()
    home = Ui_Home()
    home.setupUi(Qhome)
    web = Ui_Web()

    # Init dialog window
    Qdialog = QtWidgets.QDialog()
    dialog = Ui_Dialog()
    dialog.setupUi(Qdialog)

    # Link widgets to funtions
    home.btnLED.clicked.connect(lambda: Arduino('leds'))
    home.btnLaser.clicked.connect(lambda: Arduino('laser'))
    home.btnWeb.clicked.connect(lambda: Browser('localhost:3000'))

    home.actionQuit.triggered.connect(Qapp.exit)
    home.actionAbout.triggered.connect(Qdialog.show)
    home.actionSave.triggered.connect(Plot)

    # Load main window
    Qhome.setWindowTitle(config['app_name'])
    Qhome.show()
    Qapp.exec_()
    config.save(sort_keys=False)

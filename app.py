import os
import random
import sys
import sqlite3

from PyQt5 import QtGui, QtCore, QtWidgets, QtWebEngineWidgets
from helper import *
from plotter import *
log = Log(config['logfile'])

from dialog import Ui_Dialog
from home import Ui_Home

class Ui_Web(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):

        super(Ui_Web, self).__init__(*args, **kwargs)

        self.setWindowTitle('Mini Browser')
        self.setGeometry(5, 30, 1355, 730)

        self.browser = QtWebEngineWidgets.QWebEngineView()

        self.setCentralWidget(self.browser)

    def goTo(self, url):
        self.browser.load(QtCore.QUrl(url))


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

def LogSomething():
    con = sqlite3.connect("app.db")
    cur = con.cursor()
    res = cur.execute("SELECT title FROM movie")
    records = res.fetchall()
    for row in records:
        log.File(row[0])
    con.close()

if __name__ == '__main__':
    # Init main window
    Qapp = QtWidgets.QApplication(sys.argv)
    Qhome = QtWidgets.QMainWindow()
    home = Ui_Home()
    home.setupUi(Qhome)
    web = Ui_Web()

    for i in range(len(cmds)):
        btn = QtWidgets.QPushButton('btn%s' % cmds[i])            
        btn.setText(cmds[i])
        btn.clicked.connect(lambda: Arduino(cmds[i]))
        home.layBtns.addWidget(btn)

    # Init dialog window
    Qdialog = QtWidgets.QDialog()
    dialog = Ui_Dialog()
    dialog.setupUi(Qdialog)

    # Link widgets to funtions
    home.btnWeb.clicked.connect(lambda: Browser('https://www.yahoo.com'))
    home.actionOpen.triggered.connect(Plot)
    home.actionSave.triggered.connect(LogSomething)
    home.actionQuit.triggered.connect(Qapp.exit)
    home.actionAbout.triggered.connect(Qdialog.show)

    # Load main window
    Qhome.setWindowTitle(config['app_name'])
    Qhome.show()
    Qapp.exec_()
    config.save(sort_keys=False)

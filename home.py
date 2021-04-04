# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Sandbox\home.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(1593, 1057)
        Home.setMinimumSize(QtCore.QSize(588, 413))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        Home.setFont(font)
        Home.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(Home)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tab1 = QtWidgets.QTabWidget(self.centralwidget)
        self.tab1.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tab1.setMovable(False)
        self.tab1.setObjectName("tab1")
        self.tabLED = QtWidgets.QWidget()
        self.tabLED.setObjectName("tabLED")
        self.btnLED = QtWidgets.QPushButton(self.tabLED)
        self.btnLED.setGeometry(QtCore.QRect(30, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.btnLED.setFont(font)
        self.btnLED.setMouseTracking(False)
        self.btnLED.setAcceptDrops(False)
        self.btnLED.setAutoFillBackground(False)
        self.btnLED.setStyleSheet("background-color: rgb(0, 255, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main/icons/power.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLED.setIcon(icon)
        self.btnLED.setAutoDefault(False)
        self.btnLED.setDefault(False)
        self.btnLED.setFlat(False)
        self.btnLED.setObjectName("btnLED")
        self.btnLaser = QtWidgets.QPushButton(self.tabLED)
        self.btnLaser.setGeometry(QtCore.QRect(30, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.btnLaser.setFont(font)
        self.btnLaser.setMouseTracking(False)
        self.btnLaser.setAcceptDrops(False)
        self.btnLaser.setAutoFillBackground(False)
        self.btnLaser.setStyleSheet("background-color: rgb(255, 0, 0);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/main/icons/target.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLaser.setIcon(icon1)
        self.btnLaser.setAutoDefault(False)
        self.btnLaser.setDefault(False)
        self.btnLaser.setFlat(False)
        self.btnLaser.setObjectName("btnLaser")
        self.tab1.addTab(self.tabLED, "")
        self.tabCtl = QtWidgets.QWidget()
        self.tabCtl.setObjectName("tabCtl")
        self.dial1 = QtWidgets.QDial(self.tabCtl)
        self.dial1.setGeometry(QtCore.QRect(9, 9, 100, 100))
        self.dial1.setMinimumSize(QtCore.QSize(41, 41))
        self.dial1.setAutoFillBackground(False)
        self.dial1.setTracking(False)
        self.dial1.setOrientation(QtCore.Qt.Vertical)
        self.dial1.setInvertedAppearance(False)
        self.dial1.setInvertedControls(False)
        self.dial1.setWrapping(False)
        self.dial1.setNotchesVisible(True)
        self.dial1.setObjectName("dial1")
        self.comboBox = QtWidgets.QComboBox(self.tabCtl)
        self.comboBox.setGeometry(QtCore.QRect(110, 30, 75, 18))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tab1.addTab(self.tabCtl, "")
        self.gridLayout_2.addWidget(self.tab1, 0, 0, 1, 1)
        Home.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Home)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1593, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Home.setMenuBar(self.menubar)
        self.actionAbout = QtWidgets.QAction(Home)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/main/icons/alert round.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon2)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOpen = QtWidgets.QAction(Home)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/main/icons/open folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.actionOpen.setFont(font)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(Home)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/main/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon4)
        self.actionSave.setObjectName("actionSave")
        self.actionQuit = QtWidgets.QAction(Home)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/main/icons/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon5)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Home)
        self.tab1.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        self.btnLED.setToolTip(_translate("Home", "Toggle LEDs"))
        self.btnLED.setText(_translate("Home", "LEDs"))
        self.btnLaser.setToolTip(_translate("Home", "Toggle laser"))
        self.btnLaser.setText(_translate("Home", "Laser"))
        self.tab1.setTabText(self.tab1.indexOf(self.tabLED), _translate("Home", "LED"))
        self.comboBox.setItemText(0, _translate("Home", "gasdkjakl"))
        self.comboBox.setItemText(1, _translate("Home", "gsagag"))
        self.comboBox.setItemText(2, _translate("Home", "ahhf"))
        self.comboBox.setItemText(3, _translate("Home", "hfdah"))
        self.comboBox.setItemText(4, _translate("Home", "ah"))
        self.comboBox.setItemText(5, _translate("Home", "ahfdh"))
        self.comboBox.setItemText(6, _translate("Home", "ah"))
        self.tab1.setTabText(self.tab1.indexOf(self.tabCtl), _translate("Home", "Controls"))
        self.menuFile.setTitle(_translate("Home", "File"))
        self.menuView.setTitle(_translate("Home", "View"))
        self.menuHelp.setTitle(_translate("Home", "Help"))
        self.actionAbout.setText(_translate("Home", "About"))
        self.actionOpen.setText(_translate("Home", "Open"))
        self.actionSave.setText(_translate("Home", "Save"))
        self.actionQuit.setText(_translate("Home", "Quit"))
import res_rc

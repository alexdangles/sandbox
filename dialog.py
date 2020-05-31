# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Projects\Learning\Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(384, 88)
        Dialog.setMinimumSize(QtCore.QSize(384, 88))
        Dialog.setMaximumSize(QtCore.QSize(384, 88))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lblMessage = QtWidgets.QLabel(Dialog)
        self.lblMessage.setGeometry(QtCore.QRect(20, 20, 47, 14))
        self.lblMessage.setObjectName("lblMessage")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.close)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.lblMessage.setText(_translate("Dialog", "Question"))
import res

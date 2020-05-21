import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from MainWindow import Ui_MainWindow


def sayHello():
    print("aaddahgas")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton3.clicked.connect(sayHello)
    ui.statusbar.setVisible(False)
    MainWindow.show()
    sys.exit(app.exec_())

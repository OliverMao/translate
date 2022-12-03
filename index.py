import PyQt5
import sys
import class_main
import class_wordBook
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox,QWidget
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainUI=class_main.MainWindow()
    mainUI.show()
    sys.exit(app.exec_())
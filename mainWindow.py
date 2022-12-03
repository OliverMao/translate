# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QIcon('ico.ico'))
        MainWindow.resize(719, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.translate_button = QtWidgets.QPushButton(self.centralwidget)
        self.translate_button.setGeometry(QtCore.QRect(300, 270, 111, 41))
        font = QtGui.QFont()
        font.setFamily("033-上首方糖体")
        font.setPointSize(14)
        self.translate_button.setFont(font)
        self.translate_button.setStyleSheet("QPushButton{\n"
"border-style: outset;\n"
"background-color:rgb(194, 255, 253);\n"
"border-radius: 10px;  border: 2px groove gray;\n"
"}")
        self.translate_button.setObjectName("translate_button")
        self.output_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.output_text.setGeometry(QtCore.QRect(440, 20, 261, 551))
        font = QtGui.QFont()
        font.setFamily("033-上首方糖体")
        font.setPointSize(20)
        self.output_text.setFont(font)
        self.output_text.setStyleSheet("QTextBrowser{\n"
"background-color:rgb(247, 220, 255);\n"
"    border-radius: 10px;  border: 2px groove gray;\n"
"}")
        self.output_text.setObjectName("output_text")
        self.sel_language = QtWidgets.QComboBox(self.centralwidget)
        self.sel_language.setGeometry(QtCore.QRect(300, 150, 111, 51))
        font = QtGui.QFont()
        font.setFamily("033-上首方糖体")
        font.setPointSize(14)
        self.sel_language.setFont(font)
        self.sel_language.setStyleSheet("QComboBox{\n"
"    background-color: rgb(255, 251, 147);\n"
"        border-radius: 10px;  border: 2px groove gray;\n"
"        border-style: outset;\n"
"\n"
"}")
        self.sel_language.setObjectName("sel_language")
        self.add_word_book = QtWidgets.QPushButton(self.centralwidget)
        self.add_word_book.setGeometry(QtCore.QRect(300, 320, 111, 41))
        font = QtGui.QFont()
        font.setFamily("033-上首方糖体")
        font.setPointSize(14)
        self.add_word_book.setFont(font)
        self.add_word_book.setStyleSheet("QPushButton{\n"
"border-style: outset;\n"
"background-color:rgb(147, 203, 255);\n"
"border-radius: 10px;  border: 2px groove gray;\n"
"}")
        self.add_word_book.setObjectName("add_word_book")
        self.watch_word_book = QtWidgets.QPushButton(self.centralwidget)
        self.watch_word_book.setGeometry(QtCore.QRect(300, 370, 111, 41))
        font = QtGui.QFont()
        font.setFamily("033-上首方糖体")
        font.setPointSize(14)
        self.watch_word_book.setFont(font)
        self.watch_word_book.setStyleSheet("QPushButton{\n"
"border-style: outset;\n"
"background-color:rgb(134, 255, 215);\n"
"border-radius: 10px;  border: 2px groove gray;\n"
"}")
        self.watch_word_book.setObjectName("watch_word_book")
        self.input_text = QtWidgets.QTextEdit(self.centralwidget)
        self.input_text.setGeometry(QtCore.QRect(20, 20, 261, 551))
        font = QtGui.QFont()
        font.setFamily("033-上首方糖体")
        font.setPointSize(20)
        self.input_text.setFont(font)
        self.input_text.setStyleSheet("QTextEdit{\n"
"    background-color: rgb(255, 176, 160);\n"
"border-radius: 10px;  border: 2px groove gray;\n"
"}")
        self.input_text.setObjectName("input_text")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 220, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Yoobit翻译——From:贾镇宇"))
        self.translate_button.setText(_translate("MainWindow", "翻译"))
        self.add_word_book.setText(_translate("MainWindow", "加入单词本"))
        self.watch_word_book.setText(_translate("MainWindow", "查看单词本"))
        self.label.setText(_translate("MainWindow", "-->"))


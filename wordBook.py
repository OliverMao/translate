# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wordBook.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowIcon(QIcon('ico.ico'))
        Form.resize(463, 486)
        self.word_view = QtWidgets.QListView(Form)
        self.word_view.setGeometry(QtCore.QRect(20, 10, 431, 361))
        font = QtGui.QFont()
        font.setFamily("033-上首方糖体")
        font.setPointSize(20)
        self.word_view.setFont(font)
        self.word_view.setStyleSheet("QListView{\n"
"        background-color: rgb(216, 255, 249);\n"
"border-radius: 10px;  border: 2px groove gray;\n"
"}")
        self.word_view.setObjectName("word_view")
        self.del_word = QtWidgets.QPushButton(Form)
        self.del_word.setGeometry(QtCore.QRect(20, 430, 101, 41))
        font = QtGui.QFont()
        font.setFamily("033-上首方糖体")
        font.setPointSize(16)
        self.del_word.setFont(font)
        self.del_word.setStyleSheet("QPushButton{\n"
"border-style: outset;\n"
"background-color:rgb(255, 252, 207);\n"
"border-radius: 10px;  border: 2px groove gray;\n"
"}")
        self.del_word.setObjectName("del_word")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 380, 141, 41))
        font = QtGui.QFont()
        font.setFamily("033-上首方糖体")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.now_word = QtWidgets.QLabel(Form)
        self.now_word.setGeometry(QtCore.QRect(130, 390, 201, 21))
        font = QtGui.QFont()
        font.setFamily("033-上首方糖体")
        font.setPointSize(18)
        self.now_word.setFont(font)
        self.now_word.setObjectName("now_word")
        self.share_button = QtWidgets.QPushButton(Form)
        self.share_button.setGeometry(QtCore.QRect(150, 430, 101, 41))
        font = QtGui.QFont()
        font.setFamily("033-上首方糖体")
        font.setPointSize(16)
        self.share_button.setFont(font)
        self.share_button.setStyleSheet("QPushButton{\n"
"border-style: outset;\n"
"background-color:rgb(255, 201, 233);\n"
"border-radius: 10px;  border: 2px groove gray;\n"
"}")
        self.share_button.setObjectName("share_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "我的单词本"))
        self.del_word.setText(_translate("Form", "记住了"))
        self.label.setText(_translate("Form", "当前单词："))
        self.now_word.setText(_translate("Form", "TextLabel"))
        self.share_button.setText(_translate("Form", "分享"))


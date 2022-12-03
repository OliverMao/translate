from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox,QFileDialog
from PyQt5.QtCore import QStringListModel
import sqlite3
import wordBook
import os
from getPicture import getPicture

class WordBook(QMainWindow, wordBook.Ui_Form):
    def __init__(self, parent=None):
        self.uid=1
        super(WordBook, self).__init__(parent)
        self.setupUi(self)
        self.del_word.clicked.connect(self.delWord)
        self.word_view.clicked.connect(self.selWord)
        self.share_button.clicked.connect(self.share)
        self.getWord()
        self.sel_word=0
        self.now_word.setText('暂未选择')

    def selWord(self,qModelIndex):
        word=self.wordList[qModelIndex.row()]
        self.sel_word=word
        self.now_word.setText(word)

    def delWord(self):
        if(self.sel_word==0):
            return 1
        else:
            conn = sqlite3.connect('userWordBook.db')
            cur = conn.cursor()
            uid=self.uid
            sql="DELETE FROM word WHERE uid = "+str(uid)+" AND word_info='"+self.sel_word+"';"
            cur.execute(sql)
            conn.commit()
            conn.close()
            self.getWord()

    def getWord(self):
        conn = sqlite3.connect('userWordBook.db')
        cur = conn.cursor()
        uid=self.uid
        sql="SELECT word_info FROM word WHERE uid="+str(uid)+""
        r=cur.execute(sql)
        conn.commit()
        if(r):
            wordList=[]
            for i in r:
                # print(i[0])
                wordList.append(i[0])
            self.wordList=wordList
            slm = QStringListModel()
            slm.setStringList(wordList)
            self.word_view.setModel(slm)
        conn.close()

    def share(self):
        if(self.sel_word==0):
            return 1
        else:
            path=str(getPicture(self.sel_word))
            print(path)
            os.startfile(path)
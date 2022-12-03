from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox,QFileDialog
from PyQt5.QtCore import QStringListModel
from mainWindow import Ui_MainWindow
import json
import sqlite3
import class_wordBook
from PyQt5.QtGui import QIcon
from volcengine.ApiInfo import ApiInfo
from volcengine.Credentials import Credentials
from volcengine.ServiceInfo import ServiceInfo
from volcengine.base.Service import Service

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.translate_button.clicked.connect(self.translate)
        self.sel_language.addItems(['英译汉','汉译英'])
        self.add_word_book.clicked.connect(self.addToWordBook)
        self.watch_word_book.clicked.connect(self.watchWordBook)
        self.wordBookUi=class_wordBook.WordBook()

    def translate(self):
        self.output_text.setText('')
        data=self.input_text.toPlainText()
        k_access_key = 'YOUR ACCESS KEY'
        k_secret_key = 'YOUR SECRET KEY'
        k_service_info = \
            ServiceInfo('open.volcengineapi.com',
                        {'Content-Type': 'application/json'},
                        Credentials(k_access_key, k_secret_key, 'translate', 'cn-north-1'),
                        5,
                        5)
        k_query = {
            'Action': 'TranslateText',
            'Version': '2020-06-01'
        }
        k_api_info = {
            'translate': ApiInfo('POST', '/', k_query, {}, {})
        }
        if(self.sel_language.currentText()=='英译汉'):
            TargetLanguage='zh'
        else:
            TargetLanguage='en'
        service = Service(k_service_info, k_api_info)
        TextList=[]
        TextList.append(data)
        body = {
            'TargetLanguage': TargetLanguage,
            'TextList': TextList,
        }
        res = service.json('translate', {}, json.dumps(body))
        res=json.loads(res)
        self.output_text.setText(res['TranslationList'][0]['Translation'])

    def addToWordBook(self):
        conn = sqlite3.connect('userWordBook.db')
        cur = conn.cursor()
        old=self.input_text.toPlainText()
        new=self.output_text.toPlainText()
        if(len(old)<1 or len(new)<1):
            msg_box = QMessageBox(QMessageBox.Critical, '错误', '无单词信息')
            msg_box.exec_()
        else:
            word=old+'---'+new
            uid=1
            sql="INSERT INTO word (uid,word_info) VALUES ("+str(uid)+",'"+word+"');"
            cur.execute(sql)
            msg_box = QMessageBox(QMessageBox.Information, '成功', '已加入单词本')
            msg_box.setWindowIcon(QIcon("ico.ico"))
            msg_box.exec_()
        conn.commit()
        conn.close()

    def watchWordBook(self):
        self.wordBookUi.getWord()
        self.wordBookUi.show()

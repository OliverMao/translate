import sqlite3

conn = sqlite3.connect('userWordBook.db')
cur = conn.cursor()
sql_text_1 = '''CREATE TABLE word
            (uid NUMBER,
            word_info TEXT);'''
cur.execute(sql_text_1)
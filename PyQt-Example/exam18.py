"""
PyQt5(18. 데이터베이스-테이블 생성)
"""

import sys, pymssql
from PyQt5.QtWidgets import QApplication, QWidget


class sql(QWidget):

    def __init__(self):
        super().__init__()
        self.sqlConnect()
        self.initUI()
        self.run()


    def sqlConnect(self):

        try:
            self.conn = pymssql.connect(server='localhost', user='sa', password='318123!@#', database='WebDB_MOI')
        except:
            print("문제가 있습니다!")
            exit(1)

        print("연결 성공!")
        self.cur = self.conn.cursor() ## 현재 커서 위치를 가져옴

    def initUI(self):
        self.setGeometry(300, 300, 500, 520)
        self.setWindowTitle("데이터 베이스 활용 예제")
        self.show()


    def run(self):

        self.cmd = 'select * from jobs'

        self.cur.execute(self.cmd)
        print(self.cur.fetchall())
        self.conn.close()

app = QApplication(sys.argv)
w = sql()
sys.exit(app.exec_())
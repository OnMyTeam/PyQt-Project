"""
PyQt5(21.레코드 탐색, 삭제, 수정)
"""

import sys, pymssql
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class insert(QWidget):
    global w

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        self.w = 400
        self.h = 420
        self.btnSize = 40

        self.lblNum = QLabel("번호", self)
        self.lblNum.move(25, 25)
        self.txtNum = QLineEdit(self)
        self.txtNum.move(25 + 49, 22)
        self.txtNum.setReadOnly(True)
        self.lblName = QLabel("이름", self)
        self.lblName.move(25, 60)
        self.txtName = QLineEdit(self)
        self.txtName.move(25 + 49, 57)
        self.lblAddr = QLabel("주소", self)
        self.lblAddr.move(25, 95)
        self.txtAddr = QLineEdit(self)
        self.txtAddr.move(25 + 49, 92)

        self.btnInsert = QPushButton("입력", self)
        self.btnInsert.move(85, 130)
        self.btnInsert.clicked.connect(self.into)

        self.setGeometry(800, 330, 300, 180)
        self.setWindowTitle("데이터 베이스 활용 예제")


    def into(self):
        if (self.txtName.text() !="") and (self.txtAddr.text() !=""):
            try:
                self.cmd = "insert into MyTable01(A1,A2,A3) values({},'{}','{}')".format(self.txtNum.text(),self.txtName.text(),self.txtAddr.text())
                print(self.cmd)
                w.cur.execute(self.cmd)
                w.conn.commit()
            except:
                QMessageBox.information(self, "삽입 오류","올바른 입력으로 하세요!"),QMessageBox.Yes, QMessageBox.Yes
            return

        else:
            QMessageBox.information(self, "입력 오류", "빈칸없이 입력하세요!"), QMessageBox.Yes, QMessageBox.Yes
            return

        self.close()


    def showEvent(self, QShowEvent):

        self.txtNum.setText(str(w.cnt[0]+1))
        self.txtName.clear() ## 테스트 상자를 지움
        self.txtAddr.clear() ## 테스트 상자를 지움








class sql(QWidget):

    def __init__(self):
        super().__init__()
        self.sqlConnect()
        self.initUI()
        self.run()

    def sqlConnect(self):

        try:
            self.conn = pymssql.connect(server='localhost', user='sa', password='318123!@#', database='CustomDB')
        except:
            print("문제가 있습니다!")
            exit(1)

        print("연결 성공!")
        self.cur = self.conn.cursor()  ## 현재 커서 위치를 가져옴

    def initUI(self):

        self.w = 400
        self.h = 420
        self.btnSize = 40

        self.lblNum = QLabel("번호", self)
        self.lblNum.move(25, 25)
        self.txtNum = QLineEdit(self)
        self.txtNum.move(25 + 49, 22)
        self.lblName = QLabel("이름", self)
        self.lblName.move(25, 60)
        self.txtName = QLineEdit(self)
        self.txtName.move(25 + 49, 57)
        self.lblAddr = QLabel("주소", self)
        self.lblAddr.move(25, 95)
        self.txtAddr = QLineEdit(self)
        self.txtAddr.move(25 + 49, 92)

        self.List = QTreeView(self)  ## 특정목록을 나열해 주는 역할! 데이터를 계층적으로 표시
        self.List.setRootIsDecorated(False)  ## True을 하면 들여쓰기가됨?
        self.List.setAlternatingRowColors(True)  ## 붙어있는 데이터의 구분을 위해서 추가함
        self.List.resize(330, 200)
        self.List.move(25, 130)

        self.content = QStandardItemModel(0, 3, self)  ## QTreeView에 데이터를 나열 할수 있도록 도와줌
        self.content.setHeaderData(0, Qt.Horizontal, "번호")
        self.content.setHeaderData(1, Qt.Horizontal, "이름")
        self.content.setHeaderData(2, Qt.Horizontal, "주소")
        self.List.clicked.connect(self.slt)



        self.List.setModel(self.content)  ## QTreeView에 QStandarItemModel을 등록햐여아함
        self.List.setColumnWidth(0, 40)  ## 열의 넓이 지정함
        self.List.setColumnWidth(0, 80)  ## 행의 넓이 지정하

        self.cmdPre = QPushButton("이전", self)
        self.cmdPre.resize(self.btnSize, self.btnSize)
        self.cmdPre.clicked.connect(self.pre)
        self.cmdAft = QPushButton("다음", self)
        self.cmdAft.resize(self.btnSize, self.btnSize)
        self.cmdAft.clicked.connect(self.next)
        self.cmdNew = QPushButton("신규", self)
        self.cmdNew.resize(self.btnSize, self.btnSize)
        self.cmdNew.clicked.connect(self.new)
        self.cmdMod = QPushButton("수정", self)
        self.cmdMod.resize(self.btnSize, self.btnSize)
        self.cmdMod.clicked.connect(self.edit)
        self.cmdDel = QPushButton("삭제", self)
        self.cmdDel.resize(self.btnSize, self.btnSize)
        self.cmdDel.clicked.connect(self.dlt)

        self.cur.execute("select max(A1) from MyTable01")
        self.cnt = self.cur.fetchone()[0]

        self.setGeometry(300, 300, 500, 520)
        self.setWindowTitle("데이터 베이스 활용 예제")
        self.show()

    def slt(self):
        self.txtNum.setText(str(self.content.index(self.List.currentIndex().row(), 0).data())) ## 클릭한 행번호와 열번호의 값을 가져옴
        self.txtName.setText(str(self.content.index(self.List.currentIndex().row(), 1).data()))
        self.txtAddr.setText(str(self.content.index(self.List.currentIndex().row(), 2).data()))

    def pre(self):
        if self.List.currentIndex().row() == 0:
            return
        else:
            self.List.setCurrentIndex(self.content.index(self.List.currentIndex().row() - 1, 0))
            self.slt()
    def dlt(self):
        a = QMessageBox.question(self,"삭제 확인", "정말로 삭제 합니까?", QMessageBox.Yes |QMessageBox.No, QMessageBox.No)

        if a == QMessageBox.Yes:
            self.cmd = "delete from MyTable01 where A1='{}'".format(self.txtNum.text())
            print(self.cmd)
            self.cur.execute(self.cmd)
            self.conn.commit()
            self.cnt = self.cnt - 1
            self.content.removeRow(self.cnt)
            self.pre()
    def edit(self):
        if (self.txtName.text() !="") and (self.txtAddr.text() !=""):
            try:
                self.cmd = "update MyTable01 set A2 = '{}',A3 = '{}' where A1='{}'"\
                    .format(self.txtName.text(), self.txtAddr.text(), self.txtNum.text())
                print(self.cmd)
                self.cur.execute(self.cmd)
                self.conn.commit()
            except:
                QMessageBox.information(self, "삽입 오류", "올바른 형식으로 입력하세요.",
                                        QMessageBox.Yes, QMessageBox.Yes)
        else:
            QMessageBox.information(self, "입력 오류", "빈칸없이 입력하세요.",
                                    QMessageBox.Yes, QMessageBox.Yes)

        QMessageBox.information(self, "수정 성공", "수정되었습니다.",
                                QMessageBox.Yes, QMessageBox.Yes)

    def next(self):

        if self.List.currentIndex().row() == self.cnt - 1:
            return
        else:
            self.List.setCurrentIndex(self.content.index(self.List.currentIndex().row() + 1,0))
            self.slt()
    def new(self):

        self.cur.execute("select count(*) from MyTable01") ## TESTTABLE 데이터의 행갯수를 구함
        self.cnt = self.cur.fetchone()
        k.show()

    def resizeEvent(self, QResizeEvent):  ## 프로그램의 사이즈가 변경될때 자동으로 호출됨

        self.btnX = self.width() - 220
        self.btnY = self.height() - 60

        self.cmdPre.move(self.btnX, self.btnY)
        self.cmdAft.move(self.btnX + self.btnSize * 1, self.btnY)
        self.cmdNew.move(self.btnX + self.btnSize * 2, self.btnY)
        self.cmdMod.move(self.btnX + self.btnSize * 3, self.btnY)
        self.cmdDel.move(self.btnX + self.btnSize * 4, self.btnY)

    def closeEvent(self, QCloseEvent):
        self.conn.close()



    def enterEvent(self, QEvent): ## 창이 활성화 될때마다 호출됨

        self.cmd = "SELECT * FROM MyTable01"
        self.cur.execute(self.cmd)
        result = self.cur.fetchall()
        for i,k in enumerate(result):

            self.content.removeRow(i)
            self.content.insertRow(i)
            self.content.setData(self.content.index(i, 0), i+1)
            self.content.setData(self.content.index(i, 1), k[1])
            self.content.setData(self.content.index(i, 2), k[2])

    def run(self):

        self.cmd = "SELECT * FROM MyTable01"
        self.cur.execute(self.cmd)

        # print(self.cur.fetchall())


app = QApplication(sys.argv)
w = sql()
k = insert()
sys.exit(app.exec_())
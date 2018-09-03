"""
PyQt5(14. 버튼반복생성)
"""

import sys, random, pickle
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Exam(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):


        self.btnTop = 100
        self.cnt = 0

        self.lbl = QLabel("생성 될 버튼의 수를 입력하세요.", self)
        self.lbl.move(10, 10)

        self.txt = QLineEdit("", self)
        self.txt.move(10, self.lbl.height())

        self.btn = QPushButton("button 생성", self)

        self.btn.resize(QSize(80, 25))
        self.btn.move(10, self.lbl.height() + self.txt.height())
        self.btn.clicked.connect(self.createBtn)


        self.btn1 = QPushButton("button 없애기", self)

        self.btn1.resize(QSize(80, 25))
        self.btn1.move(self.btn.width()+10 , self.lbl.height() + self.txt.height())

        self.btn1.clicked.connect(self.deleteBtn)
        self.setGeometry(1400, 250, 320, 200)
        self.show()

    def createBtn(self):

        self.cnt = int(self.txt.text())
        self.btnList = []
        self.LastSize = 0

        for i in range(self.cnt):
            self.btnList.append(QPushButton(str(i + 1)+"번째 버튼", self))
            self.btnList[i].resize(QSize(80, 25))

            self.btnList[i].move(10, self.btnTop + (i * 25))

            self.btnList[i].show()
        else:
            self.setGeometry(1400, 250, 320, self.btnTop + (i * 25) + 50)

    def deleteBtn(self):
        for i in range(self.cnt):
            self.btnList[i].deleteLater()
            self.setGeometry(1400, 250, 320, self.lbl.height() + self.txt.height() + self.btn1.height()+ 50)

app = QApplication([])
ex = Exam()
sys.exit(app.exec_())
"""
PyQt5(13. 그레이스케일, 파일 불러오기)
"""

import sys, random, pickle
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QPushButton
from PyQt5.QtCore import Qt, QBasicTimer, QDate
from PyQt5.QtGui import *


class Exam(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):

        self.sid = QImage("C:/Users/10160081/Documents/받은 파일/C4B981E0.PNG").scaled(120, 120)
        btn = QPushButton("이미지 변경", self)
        btn.resize(btn.sizeHint())
        btn.move(20, 150)
        btn.clicked.connect(self.openFileNameDialog)
        self.setGeometry(1400, 250, 320, 200)
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawImages(painter)
        painter.end()

    def drawImages(self, painter):
        painter.drawImage(5, 15, self.sid)
        painter.drawImage(self.sid.width() +10, 15, self.grayScale(self.sid.copy()))

    def grayScale(self, image):

        for i in range(self.sid.width()):
            for j in range(self.sid.height()):

                c = image.pixel(i, j)
                gray = qGray(c)
                alpha = qAlpha(c)
                image.setPixel(i, j, qRgba(gray, gray, gray, alpha))

        return image

    def openFileNameDialog(self):

        fileName, _ = QFileDialog.getOpenFileName(self, "불러올 이미지를 선택하세요.","","All Files (*);;Python Files (*.py)")

        if fileName:
            print(fileName)
            self.sid = QImage(fileName).scaled(120, 120)

app = QApplication([])
ex = Exam()
sys.exit(app.exec_())
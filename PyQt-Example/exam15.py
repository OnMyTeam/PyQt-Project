"""
PyQt5(15. 이미지 반사시키기)
"""

import sys, random, pickle
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Exam(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.createReflectImage()

    def initUI(self):


        self.img = QImage("C:/Users/sangi/OneDrive/Clouds_minimalistic_binary_storage_2560x1600.jpg") ## 이미지 객체를 생성한다
        if self.img.isNull(): ## 이미지가 없다면 에러메세지 출력후 프로그램 종료
            print("Error loading image")
            sys.exit(1)

        self.iw = self.img.width() ## 이미지 가로 사이즈
        self.ih = self.img.height() ## 이미지 세로 사이즈즈

        self.setGeometry(500, 250, 320, 450)
        self.show()

    def createReflectImage(self):


        self.refImage = QImage(self.iw, self.ih, QImage.Format_ARGB32)

        painter = QPainter()
        painter.begin(self.refImage)
        painter.drawImage(0, 0, self.img)
        painter.begin(self.refImage)
        painter.drawImage(0, 0, self.img)

        painter.setCompositionMode(QPainter.CompositionMode_DestinationIn)
        gradient = QLinearGradient(self.iw / 2, 0, self.iw / 2, self.ih)

        gradient.setColorAt(1, QColor(0, 0, 0))
        gradient.setColorAt(0, Qt.transparent)

        painter.fillRect(0, 0, self.iw, self.ih, gradient)

        painter.end()

    def paintEvent(self, event): ## Painter 객체 생성후 이미지 그리는 draw 함수를 호출한다.

        painter = QPainter()
        painter.begin(self)
        self.draw(painter)
        painter.end()

    def draw(self, painter):
        painter.drawImage(25, 15, self.img)
        painter.translate(0, 2 * self.ih + 15)
        painter.scale(1, -1) ## 
        painter.drawImage(25, 0, self.refImage)



app = QApplication([])
ex = Exam()
sys.exit(app.exec_())
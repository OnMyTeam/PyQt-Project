"""
PyQt5(11. 페인터)
"""
import sys, random
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QGridLayout, \
    QInputDialog, QLineEdit, QFrame, QColorDialog, QSizePolicy, QLabel, QFontDialog, QCheckBox, QProgressBar, \
    QCalendarWidget, QComboBox
from PyQt5.QtCore import Qt, QBasicTimer, QDate
from PyQt5.QtGui import QColor, QPixmap, QPainter, QFont, QPen, QBrush


class Exam(QWidget):  ## 이미지 표시

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.a = "쉽고 재밌는 IT 교육채널 \n리턴제로"


        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Drawing Text')
        self.show()

    def paintEvent(self, event):

        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        self.drawPoints(qp)
        self.drawRectangles(qp)
        self.drawLines(qp)
        self.drawBrushed(qp)
        qp.end()

    def drawText(self, event, qp):
        qp.setPen(QColor(168, 35, 3))
        qp.setFont(QFont('gulim',10))
        qp.drawText(event.rect(), Qt.AlignCenter, self.a)

    def drawPoints(self, qp):
        qp.setPen(Qt.red) ## Pen의 색을 Color 상수로 지정함
        size = self.size() ## 현재창의 사이즈를 구함

        for i in range(1000):
            x = random.randint(0, size.width()) ## 0부터 가로 사이즈의 랜덤
            y = random.randint(0, size.height()) #3 0부터 세로 사이즈의 랜덤
            qp.drawPoint(x, y) ## 좌표값을 넣어 점을 찍음


    def drawRectangles(self, qp):

        col = QColor()
        col.setNamedColor('#521E8D') ## 펜의색을 16진수로 지정
        qp.setPen(col)

        qp.setBrush(QColor(200, 0, 0))
        qp.drawRect(10, 45, 90, 60)

        qp.setBrush(QColor(255, 80, 0, 160))
        qp.drawRect(130, 45, 90, 60)

        qp.setBrush(QColor(25, 0, 90, 200))
        qp.drawRect(250, 45, 90, 60)

    def drawLines(self, qp):

        pen = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen)
        qp.drawLine(20, 100, 250, 100)

        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(20, 140, 250, 140)

        pen.setStyle(Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 180, 250, 180)

        pen.setStyle(Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(20, 220, 250, 220)

        pen.setStyle(Qt.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 260, 250, 260)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        qp.setPen(pen)
        qp.drawLine(20, 300, 250, 300)

    def drawBrushed(self, qp):

        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 15, 90, 60)

        brush.setStyle(Qt.Dense1Pattern)
        qp.drawRect(130, 15, 90, 60)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Exam()



    sys.exit(app.exec_())
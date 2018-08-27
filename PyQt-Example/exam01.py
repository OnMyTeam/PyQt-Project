"""
PyQt5(01. 위젯창생성,버튼추가)
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        btn1 = QPushButton('첫번째버튼',self)
        btn1.resize(btn1.sizeHint())
        btn1.setToolTip('<b>마우스 툴팁입니다.</b>') #마우스 올렸을때 표시
        btn1.move(20,20)

        self.setGeometry(800,300,600,600)
        self.setWindowTitle('Exam01')
        self.show()



app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())



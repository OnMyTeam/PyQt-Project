
"""
PYQT5 공부하기(01. 위젯창생성, 버튼추가)
"""
import sys
## QtWidets 모드안에 대부분 위젯이 추가되어있음 ex) 버튼,Combobox 등등..
from PyQt5 import QtWidgets


class Example(QtWidgets.QWidget):
    def __init__(self):
        ##상위 객체 생성
        super().__init__()
        self.initUI()

    def initUI(self):
        
        btn1 = QtWidgets.QPushButton('버튼1', self)
        btn1.resize(btn1.sizeHint())
        btn1.setToolTip('툴팁입니다')
        btn1.move(25, 30)

        ##창크기 조절
        self.setGeometry(30,50,800,600)
        self.setWindowTitle('첫번째 시간~')
    
        self.show()


##Qt5어플리케이션은 QApplication을 생성햐여야함 그냥
app = QtWidgets.QApplication(sys.argv)
w = Example()
##프로그램을 깨끗히 종료하기위함
sys.exit(app.exec_())
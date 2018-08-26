"""
PYQT5 공부하기(02. 이벤트처리, 메세지박스 )
"""
import sys
## QtWidets 모드안에 대부분 위젯이 추가되어있음 ex) 버튼,Combobox 등등..
from PyQt5.QtWidgets import QWidget,QApplication,QMessageBox,QPushButton
## QCoreApplication 이벤트처리 담당
from PyQt5 import QtCore추

class Example1(QWidget):
    def __init__(self):
        ##상위 객체 생성
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('버튼1', self)
        btn1.resize(btn1.sizeHint())
        btn1.setToolTip('툴팁입니다')
        btn1.move(50, 50)
        btn1.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.show()
    ## closeEvent X버튼 눌렀을때 하고싶은것    
    def closeEvent(self, QCloseEvent):
        ans = QMessageBox.question(self,'종료확인','퇴사하시겠습니까?',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)

        if ans == QMessageBox.Yes:
            ##창 꺼짐
            QCloseEvent.accept()
        else:
            ##창 안꺼짐
            QCloseEvent.ignore()


        ##창크기 조절
        self.setGeometry(30, 50, 800, 600)
        self.setWindowTitle('첫번째 시간~')

        self.show()


##Qt5어플리케이션은 QApplication을 생성햐여야함 그냥
app = QApplication(sys.argv)
w = Example1()
##프로그램을 깨끗히 종료하기위함
sys.exit(app.exec_())
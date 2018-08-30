"""
PyQt5(07. 대화상자)
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout , QPushButton, QGridLayout,\
                            QInputDialog, QLineEdit, QFrame, QColorDialog,QSizePolicy, QLabel, QFontDialog
from PyQt5.QtGui import QColor



"""
QHBoxLayout : 가로로 차곡차곡 쌓임
QVBoxLayout : 세로로 차곡차곡 쌓임
"""

class Exam(QWidget): ## 입력할 Dialog 생성

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.btn = QPushButton("Dialog", self) ## 버튼추가
        self.btn.move(20, 20) #버튼 위치 변경
        self.btn.clicked.connect(self.showDialog) # 버튼 이벤트시 실행할 함수 연결

        self.le = QLineEdit(self)
        self.le.setText("우선디폴트!")
        self.le.move(130,22)

        self.setGeometry(300,300,300,150)
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog','Enter your name :')

        if ok:
            self.le.setText(str(text))


class Exam01(QWidget): ## 색깔 Dialog 생성

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        col = QColor(0,0,0) ## 컬러 객체 생성 RGB

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color :%s}" % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.move(300,150)
        self.setWindowTitle('Calculator')
        self.show()


    def showDialog(self):
        col = QColorDialog.getColor() ## QColorDialog 칼러 선택창을 열겠다. getColor()선택할 RGB값 가져올수 있다~

        if col.isValid(): ## 색깔 선택후 OK 누르면 True, Cancel을 누르면 False
            self.frm.setStyleSheet("QWidget { background-color :%s}"
                                   % col.name())

class Exam02(QWidget): ## Font 설정 다이얼로그 생성

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        vBox = QVBoxLayout()

        btn = QPushButton('Dialog',self)
        btn.setSizePolicy(QSizePolicy.Fixed, ## 버튼 size 고정!
                          QSizePolicy.Fixed)

        btn.move(20,20)

        vBox.addWidget(btn)
        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('Knowledge only matter', self)
        self.lbl.move(130,20)
        vBox.addWidget(self.lbl)

        self.setLayout(vBox)

        self.setGeometry(130, 22, 100, 100)

        self.move(300,150)
        self.setWindowTitle('Calculator')
        self.show()


    def showDialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.lbl.setFont(font)

            
            
            
if __name__ =='__main__':
    app = QApplication(sys.argv)
    w = Exam()
    w1 = Exam01()
    w2 = Exam02()
    sys.exit(app.exec_())
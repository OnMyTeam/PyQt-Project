"""
PyQt5(08. 여러가지 위젯 1/2)
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QGridLayout, \
    QInputDialog, QLineEdit, QFrame, QColorDialog, QSizePolicy, QLabel, QFontDialog, QCheckBox, QProgressBar,\
    QCalendarWidget
from PyQt5.QtCore import Qt, QBasicTimer, QDate
from PyQt5.QtGui import QColor


class Exam(QWidget):  ## 체크박스

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle() ## 체크 미리 해놓겠습니다
        cb.stateChanged.connect(self.changeTitle) ## 삳태가 변환되면 함수 실행

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('QCheckBox')
        self.show()

    def changeTitle(self, state):

        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')


class Exam01(QWidget):  ## 버튼 Pressed에 다른 Qframe 색깔변경

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.col = QColor(0, 0, 0)  ## 컬러 객체 생성 RGB

        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)
        redb.clicked.connect(self.setColor)

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)
        greenb.clicked.connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)
        blueb.clicked.connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150,20,100,100)
        self.square.setStyleSheet("QWidget {background-color : %s}"% self.col.name())


        self.setGeometry(300,300,280,170)
        self.setWindowTitle('Toggle button')
        self.show()




    def setColor(self, pressed):

        source = self.sender() ## 호출한 버튼의 객체를 불러옴

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame { background-color: %s}" % self.col.name())




class Exam02(QWidget):  ## Progress Bar 생성

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.pbar = QProgressBar(self) ## ProgressBar 생성
        self.pbar.setGeometry(30,40,200,25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer() ## 일정시간 단위로 계속 반복적으로 진행해야할때
        self.step = 0

        self.setGeometry(300, 300, 280, 170)

        self.setWindowTitle('QProgressBar')
        self.show()

    def timerEvent(self, e):

        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return


        self.step = self.step + 1
        self.pbar.setValue(self.step)


    def doAction(self):

        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')

        else:
            self.timer.start(100, self) ## 0.1초마다 Timer 가 실행디ㅗㅁ
            self.btn.setText('Stop ')
            
            
class Exam03(QWidget):  ## Calendar 생성

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout(self)
        cal = QCalendarWidget(self)
        cal.clicked[QDate].connect(self.showDate)


        vbox.addWidget(cal)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        vbox.addWidget(self.lbl)

        self.setLayout(vbox)


        self.setGeometry(300,300,280,170)
        self.setWindowTitle('Calendar')
        self.show()




    def showDate(self, date):

         self.lbl.setText(date.toString())

        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Exam()
    w1 = Exam01()
    w2 = Exam02()
    w3 = Exam03()
    sys.exit(app.exec_())
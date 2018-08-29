"""
PyQt5(06. 이벤트처리상세 및 시그널)
"""
import sys
from PyQt5.QtWidgets import QWidget,QLCDNumber, QSlider,QVBoxLayout, QHBoxLayout, \
                            QApplication, QGridLayout, QLabel, QPushButton, QMainWindow
from PyQt5.QtCore import Qt,pyqtSignal,QObject

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self) ## Horizontal 이기 때문에 가로로 증가

        vbox = QVBoxLayout() ## 세로로 착착착 쌓겠다.
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        #sld.valueChanged.connect(lambda: self.on_button(1))
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300,300,250,150)
        self.show()

    def on_button(self, n):
        print('Button {0} clicked'.format(n))

"""
Example1
키보드 이벤트
"""
class Example1(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(600,300,250,150)
        self.show()

    def keyPressEvent(self, QKeyEvent): ## QKeyEvent : 키보드 눌렀을떄 그 값을 받음
        print(QKeyEvent.key())
        if QKeyEvent.key() == Qt.Key_Escape:

            self.close()

"""
Example2
마우스 움직임 이벤트
"""
class Example2(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)
        x = 0
        y = 0
        self.text = "x : {0}, y : {1}".format(x,y)
        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)
        
        self.setMouseTracking(True) ## 마우스 트래킹을 함 마우스 움직일대 마다 감지함
        self.setLayout(grid)
        self.setGeometry(300,600,250,150)
        self.show()

    def mouseMoveEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        y = QMouseEvent.y()

        text = "x : {0}, y : {1}".format(x,y)
        self.label.setText(text)


"""
Example3
버튼 이벤트로 상태표시줄 변경
"""


class Example3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        btn1 = QPushButton("Button1", self)
        btn2 = QPushButton("Button2", self)
        btn1.move(30, 50)
        btn2.move(150, 50)


        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)


        self.statusBar()

        self.setGeometry(600, 600, 250, 150)
        self.show()

    def buttonClicked(self):
        sender = self.sender() ## 호출한 객체를 가지고옴 여기서는 누른 버튼에 대한 객체를 가져옴
        self.statusBar().showMessage(sender.text() + ' was pressed')


class Example4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.c = Communicate()
        self.c.closeApp.connect(self.close)


        self.setGeometry(900, 300, 250, 150)
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()

class Communicate(QObject):
    closeApp = pyqtSignal()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    w1 = Example1()
    w2 = Example2()
    w3 = Example3()
    w4 = Example4()
    sys.exit(app.exec_())
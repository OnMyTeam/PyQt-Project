"""
PyQt5(09. 여러가지 위젯 2/2)
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QGridLayout, \
    QInputDialog, QLineEdit, QFrame, QColorDialog, QSizePolicy, QLabel, QFontDialog, QCheckBox, QProgressBar, \
    QCalendarWidget, QComboBox
from PyQt5.QtCore import Qt, QBasicTimer, QDate
from PyQt5.QtGui import QColor, QPixmap


class Exam(QWidget):  ## 이미지 표시

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):


        hbox = QHBoxLayout(self)
        pixmap = QPixmap('0_0.PNG')
        pixmap1 = QPixmap('0_1.PNG')


        lbl = QLabel(self)
        lbl1 = QLabel(self)
        lbl.setPixmap(pixmap)
        lbl1.setPixmap(pixmap1)


        hbox.addWidget(lbl)
        hbox.addWidget(lbl1)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('show_Image')
        self.show()



class Exam01(QWidget):  ## QLineEdit onChanged

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.lbl = QLabel(self)
        qle = QLineEdit(self)
        qle.move(60, 100)
        self.lbl.move(60, 40)

        qle.textChanged[str].connect(self.onChange)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('onChanged QLienEdit')
        self.show()

    def onChange(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize() ## Label이 Test 사이즈에 따라서 조절됨


class Exam02(QWidget):  ## QComBoBox 생성

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.lbl = QLabel('Ubuntu', self)
        combo = QComboBox(self)
        combo.addItem('Ubuntu')
        combo.addItem('Mendriva')
        combo.addItem('Fedare')
        combo.addItem('Arch')
        combo.addItem('Genton')

        combo.move(50, 50)
        self.lbl.move(50, 150)

        combo.activated[str].connect(self.onActivated)
        self.setGeometry(300, 300, 280, 170)

        self.setWindowTitle('QProgressBar')
        self.show()

    def onActivated(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()## Label이 Test 사이즈에 따라서 조절됨




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Exam()
    w1 = Exam01()
    w2 = Exam02()

    sys.exit(app.exec_())
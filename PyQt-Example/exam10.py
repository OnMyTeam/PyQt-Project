"""
PyQt5(10. 드로그앤드롭)
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QGridLayout, \
    QInputDialog, QLineEdit, QFrame, QColorDialog, QSizePolicy, QLabel, QFontDialog, QCheckBox, QProgressBar, \
    QCalendarWidget, QComboBox
from PyQt5.QtCore import Qt, QBasicTimer, QDate, QMimeData
from PyQt5.QtGui import QColor, QPixmap, QDrag


class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)



    def mouseMoveEvent(self, e): ##버튼 위에서 마우스가 움직일때 발생하는 이벤트
        if e.buttons() != Qt.RightButton:
            return

        mimeData = QMimeData() ## 다양한 멀티데이터를 다를 수 있음?

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.exec_(Qt.MoveAction)


    def mousePressEvent(self, e):

        super().mousePressEvent(e)
        if e.buttons() == Qt.LeftButton:
            print('press')



class Exam(QWidget):  ## QLineEdit onChanged

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setAcceptDrops(True) ## Drop 이벤트 활성화
        self.button = Button('Button', self)
        self.button.move(100, 65)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('DragDrop')
        self.show()

    def dragEnterEvent(self, QDragEnterEvent): ##  Drage된 데이터를 허용함

        QDragEnterEvent.accept()

    def dropEvent(self, QDropEvent):
        position = QDropEvent.pos()
        self.button.move(position)

        QDropEvent.accept()




class Button1(QPushButton):

    def __init__(self,title, parent):
        super().__init__(title,parent)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):

        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()


    def dropEvent(self, e):

        self.setText(e.mimeData().text())

class Exam01(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button1("Button", self)
        button.move(220, 65)
        self.setGeometry(300, 300, 400, 150)
        self.setWindowTitle('DragDrop')
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Exam()
    w1 = Exam01()

    sys.exit(app.exec_())
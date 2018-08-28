"""
PyQt5(02. 이벤트처리,메세지박스)
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication ## 버튼 클릭시 slot 연결
class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn1 = QPushButton('button1',self)
        btn1.resize(btn1.sizeHint())
        btn1.move(50,50)
        btn1.clicked.connect(QApplication.instance().quit) ## connected은 slot을 연결한다.
        self.resize(500,500)
        self.setWindowTitle("PyQt5!")
        self.show()

    def closeEvent(self, QCloseEvent): ## x버튼 종료 눌렀을때 이벤트 동작
        ans = QMessageBox.question(self, "종료 확인","종료하시겠습니까?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if ans == QMessageBox.Yes ## 메세지박스에서 선택된 값을 받는다.
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
        
        
app = QApplication(sys.argv)
w = Exam()
sys.exit((app.exec_()))
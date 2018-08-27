"""
PYQT5 공부하기(03. 메뉴바, 상태표시줄)
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QMenu
from PyQt5.QtCore import QCoreApplication
class Exam(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar() # 상태표시줄(한번만 실행하면 상태표시줄 생성함)
        self.statusBar().showMessage("안녕하세요")
        menu = self.menuBar() # 메뉴바 생성
        menu_file = menu.addMenu("File") # 그룹생성
        menu_edit = menu.addMenu("Edit") # 그룹생성


        file_exit = QAction('Exit',self) # 메뉴 객체 생성
        file_exit.setShortcut('Ctrl+Q') # 단축키 지정
        file_exit.setStatusTip("누르면 나가집니다.")
        file_exit.triggered.connect(QCoreApplication.instance().quit)
        new_txt = QAction('텍스트', self)
        new_py = QAction('파이썬 파일', self)
        

        file_new = QMenu('New',self)
        file_new.addAction(new_txt) # 서브메뉴 추가
        file_new.addAction(new_py) # 서브메뉴 추가
        menu_file.addMenu(file_new) # 주 메뉴추가
        menu_file.addAction(file_exit) # Exit 기능 File그룹에 추가

        self.resize(1200,800)
        self.show()



app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())
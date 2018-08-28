"""
PyQt5(03. 메뉴바,상태표시줄)
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QMenu
from PyQt5.QtCore import QCoreApplication
class Exam(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar() ## 상태표시줄 생성
        self.statusBar().showMessage("안녕하세요!") ## 한번더 생성하면 상태표시줄 객체 생성

        menu = self.menuBar() # 메뉴바 생성
        menu_file = menu.addMenu('File') #그룹생성
        menu_edit = menu.addMenu('Edit') #그룹생성

        file_exit = QAction('Exit',self) #그룹생성 안 메뉴생성
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip("나가요~")
        file_exit.triggered.connect(QApplication.instance().quit)
        
        file_new = QMenu("New",self) # 서브그룹생성

        file_new_open = QAction('open',self)
        file_new_save = QAction('Save', self)
        file_new.addAction(file_new_open)
        file_new.addAction(file_new_save)
        menu_file.addMenu(file_new)
        menu_file.addAction(file_exit)



        self.resize(450,400)
        self.show()


app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())
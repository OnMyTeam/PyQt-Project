"""
PYQT5 공부하기(03. 메뉴바생성, 상태표시줄 추가)
"""

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QAction, QMenu
from PyQt5 import QtCore
# 상태표시줄 구현하려면 QMainWindow
class Exam(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 상태표시줄 생성
        self.statusBar()
        self.statusBar().showMessage('하이요')

        menu = self.menuBar()                           #메뉴 생성
        menu_file = menu.addMenu('File')                #그룹생성
        menu_setting = menu.addMenu('setting')          #그룹생성

        file_exit = QAction('Exit', self)               #메뉴 객체 생성
        file_exit.setShortcut('')
        file_exit.setStatusTip("ggggggggggggg")
        file_exit.triggered.connect(QtCore.QCoreApplication.instance().quit)
        new_text = QAction('파일생성', self)
        new_text_remove = QAction('파일지우기', self)


        file_new = QMenu('New', self)

        file_new.addAction(new_text)
        file_new.addAction(new_text_remove)


        menu_file.addMenu(file_new)
        menu_file.addAction(file_exit)                  #File버튼 누르면 Exit메뉴 추가

        self.resize(450,400)
        self.show()


app = QApplication(sys.argv)

w = Exam()
sys.exit(app.exec_())
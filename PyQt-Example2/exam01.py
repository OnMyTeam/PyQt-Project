import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Window"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setWindowIcon(QtGui.QIcon("Icon.jpg"))
        self.InitWindow()
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()




App = QApplication(sys.argv)
w = Window()
sys.exit(App.exec_())


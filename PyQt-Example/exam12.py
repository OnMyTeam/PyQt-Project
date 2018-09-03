"""
PyQt5(12. 테이블 위젯)
"""
import sys, random, pickle
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QGridLayout, \
    QInputDialog, QLineEdit, QFrame, QColorDialog, QSizePolicy, QLabel, QFontDialog, QCheckBox, QProgressBar, \
    QCalendarWidget, QComboBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QBasicTimer, QDate
from PyQt5.QtGui import QColor, QPixmap, QPainter, QFont, QPen, QBrush


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.size = 4
        self.initUI()

    def initUI(self):

        self.createTable()
        self.btn = QPushButton("저장")
        self.btn.clicked.connect(on_cl)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.btn)
        self.setLayout(self.layout)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Drawing Text')
        self.show()

    def createTable(self):

        self.table = QTableWidget()
        self.table.setRowCount(self.size)
        self.table.setColumnCount(self.size)
        self.table.setHorizontalHeaderLabels(('이름','국어','영어','수학'))
        try:
            fp = open("out.txt", "rb")

            for r in range(self.size):
                for c in range(self.size):
                    self.table.setItem(r, c, QTableWidgetItem(str(pickle.load(fp))))

            fp.close()

        except:
            for r in range(self.size):
                for c in range(self.size):
                    self.table.setItem(r, c, QTableWidgetItem(""))

def on_cl(self):
    fp = open("out.txt", "wb")
    for r in range(ex.size):
        for c in range(ex.size):
            pickle.dump(ex.table.item(r,c).text(), fp)
    fp.close()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()



    sys.exit(app.exec_())
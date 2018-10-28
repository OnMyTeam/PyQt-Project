import sys, random

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication, \
    QSizePolicy

from PyQt5.QtGui import QFont
from PyQt5.QtTest import QTest


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.button = []
        self.fside = ["＠", "☆", "★", "◎", "♠", "♥", "♧", "▣", "＠", "☆", "★", "◎", "♠", "♥", "♧", "▣"]
        self.cnt = 0
        self.a = 0
        self.b = 0

        for x in range(300):
            rnd = random.randint(0, 15)
            self.fside[rnd], self.fside[0] = self.fside[0], self.fside[rnd]

        self.grid = QGridLayout()
        self.grid.setSpacing(15)

        fnt = QFont()
        fnt.setBold(True)
        fnt.setPixelSize(50)

        for r in range(4):

            self.button.append([])
            for c in range(4):
                self.button[r].append(QPushButton(self.fside[r * 4 + c]))
                self.button[r][c].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.button[r][c].setFont(fnt)
                self.button[r][c].setToolTip(str(r * 4 + c))
                self.button[r][c].setToolTipDuration(1)
                self.button[r][c].clicked.connect(self.test)
                self.grid.addWidget(self.button[r][c], r, c)

        self.setLayout(self.grid)
        self.setGeometry(100, 100, 500, 500)

    def hidePzl(self):
        QTest.qWait(2000)
        for r in range(0, 4):
            for c in range(0, 4):
                self.button[r][c].setText("?")

    def test(self):

        e = self.sender()

        if e.text() != "?":
            return
        if self.cnt == 0:
            self.cnt = 1
            e.setText(self.fside[int(e.toolTop())])
            self.a = int(e.toolTip())
        else:
            self.cnt = 0
            e.setText(self.fside[int(e.toolTip())])
            self.b = int(e.toolTip())
            self.chk(self.a, self.b)

    def chk(self, a, b):
        if self.fside[a] != self.fside[b]:
            QTest.qWait(600)
            self.button[a // 4][a % 4].setText("?")
            self.button[b // 4][b % 4].setText("?")


app = QApplication([])
ex = Window()
ex.show()
ex.hidePzl()
sys.exit(app.exec_())

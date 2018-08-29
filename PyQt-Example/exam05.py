"""
PyQt5(05. 레이아웃)
"""
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QHBoxLayout,QVBoxLayout,QGridLayout,QLineEdit,QTextEdit,QLabel
"""
QHBoxLayout : 가로로 착착착 쌓임
QVBoxLayout : 세로로 착착착 쌓임
"""

class Exam(QWidget): ## QBoxLayout, QHBoxLayout

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1) ## 버튼이 있지않는 크기 만큼 영역을 차지 하게됨
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300,300,300,150)
        self.setWindowTitle("Buttons")

        self.show()



class Exam1(QWidget): ## QGridLayout

    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls','Bck','','Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '/',]

        positions = [(i,j) for i in range(5) for j in range(4)]


        for position, name in zip(positions, names):

            if name == '':
                continue

            button = QPushButton(name)
            grid.addWidget(button, *position) ## 튜플로 된 값들을 추출해냄 ex) (0,1) -> 0,1

        self.move(300,150)
        self.setWindowTitle('Calculator')
        self.show()


class Exam2(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit() ## 텍스트 상자
        authorEdit = QLineEdit() ## 텍스트 상자
        reviewEdit = QTextEdit() ## 텍스트 긴상자 remark?

        grid = QGridLayout()
        grid.setSpacing(10) ## 각각 개체들 사이에 여백을 10만큼 주겠다.

        grid.addWidget(title,1,0)
        grid.addWidget(titleEdit,1,1)

        grid.addWidget(author,2,0)
        grid.addWidget(authorEdit,2,1)

        grid.addWidget(review,3,0)
        grid.addWidget(reviewEdit,3,1,5,1)

        self.setLayout(grid)

        self.setGeometry(300,300,350,300)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Exam()
    w1 = Exam1()
    w2 = Exam2()
    sys.exit(app.exec_())
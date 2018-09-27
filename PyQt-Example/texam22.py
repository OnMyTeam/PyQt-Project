# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exam22.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(586, 234)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 90, 31))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 551, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 141, 16))
        self.label_2.setObjectName("label_2")
        self.rb_5min = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_5min.setGeometry(QtCore.QRect(10, 110, 61, 19))
        self.rb_5min.setObjectName("rb_5min")
        self.rb_3min = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_3min.setGeometry(QtCore.QRect(70, 110, 51, 19))
        self.rb_3min.setObjectName("rb_3min")
        self.rb_1min = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_1min.setGeometry(QtCore.QRect(120, 110, 51, 19))
        self.rb_1min.setObjectName("rb_1min")
        self.rb_10sec = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_10sec.setGeometry(QtCore.QRect(170, 110, 71, 19))
        self.rb_10sec.setObjectName("rb_10sec")
        self.rb_1sec = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_1sec.setGeometry(QtCore.QRect(230, 110, 51, 19))
        self.rb_1sec.setObjectName("rb_1sec")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(310, 90, 121, 51))
        self.btn_start.setObjectName("btn_start")
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(440, 90, 121, 51))
        self.btn_stop.setObjectName("btn_stop")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 541, 51))
        font = QtGui.QFont()
        font.setFamily("휴먼옛체")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.rb_5min.clicked.connect(MainWindow.setCycle)
        self.rb_3min.clicked.connect(MainWindow.setCycle)
        self.rb_1min.clicked.connect(MainWindow.setCycle)
        self.rb_10sec.clicked.connect(MainWindow.setCycle)
        self.rb_1sec.clicked.connect(MainWindow.setCycle)
        self.btn_start.clicked.connect(MainWindow.startChk)
        self.btn_stop.clicked.connect(MainWindow.stopChk)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "웹툰 감지 프로그램"))
        self.label.setText(_translate("MainWindow", "주소 입력"))
        self.label_2.setText(_translate("MainWindow", "주기를 선택하세요"))
        self.rb_5min.setText(_translate("MainWindow", "5분"))
        self.rb_3min.setText(_translate("MainWindow", "3분"))
        self.rb_1min.setText(_translate("MainWindow", "1분"))
        self.rb_10sec.setText(_translate("MainWindow", "10초"))
        self.rb_1sec.setText(_translate("MainWindow", "1초"))
        self.btn_start.setText(_translate("MainWindow", "체크 시작"))
        self.btn_stop.setText(_translate("MainWindow", "체크 종료"))
        self.label_3.setText("이 곳에 결과가 출력됩니다.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


"""
PyQt5(17. 타임벨)
"""

import sys, numpy, time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *



class Exam(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(0,0,500,520)
        self.setWindowTitle("타임벨 테스트")

        self.lblTitle = QLabel("타임벨 정지", self)
        self.lblTitle.setFont(QFont("맑은고딕", 35))
        self.lblTitle.setAlignment(Qt.AlignCenter)
        self.lblTitle.resize(350, 40)
        self.lblTitle.move(75, 10)

        self.lblNow = QLabel("", self)
        self.lblNow.setFont(QFont("맑은고딕", 45))
        self.lblNow.setAlignment(Qt.AlignCenter)
        self.lblNow.resize(350, 46)
        self.lblNow.move(75, 60)

        self.on = QPushButton("ON", self)
        self.on.setFont(QFont("맑은고딕", 24))
        self.on.resize(170, 35)
        self.on.move(75, 116)
        self.on.clicked.connect(self.timeStart)

        self.off = QPushButton("OFF", self)
        self.off.setFont(QFont("맑은고딕", 24))
        self.off.resize(170, 35)
        self.off.move(255, 116)
        self.off.clicked.connect(self.timeStop)


        self.lbl = QLabel("        요일       시작          종료            수업        "
                          "휴식       점심시작      점심종료", self)

        self.lbl.move(10, 170)

        self.day_txt = ["", "월", "화", "수", "목", "금", "토", "일"]
        self.day_chk = []
        self.day_chk.append(0)
        self.time_st = []
        self.time_st.append(0)
        self.time_ed = []
        self.time_ed.append(0)
        self.time_ls = []
        self.time_ls.append(0)
        self.time_rs = []
        self.time_rs.append(0)
        self.time_lch_st = []
        self.time_lch_st.append(0)
        self.time_lch_ed = []
        self.time_lch_ed.append(0)
        self.lch_chk = []
        self.lch_chk.append(0)

        for r in range(1, 8):

            self.day_chk.append(QCheckBox(self.day_txt[r] + "요일",self))
            self.day_chk[r].move(20, 165 + r * 28)
            self.day_chk[r].setChecked(True)
            self.time_st.append(QTimeEdit(self))
            self.time_st[r].setDisplayFormat("hh:mm")
            self.time_st[r].setTime(QTime(9, 00))
            self.time_st[r].move(20 + 70, 165 + r * 28)
            self.time_ed.append(QTimeEdit(self))
            self.time_ed[r].setDisplayFormat("hh:mm")
            self.time_ed[r].setTime(QTime(22, 00))
            self.time_ed[r].move(20 + 70 + 70, 165 + r * 28)
            self.time_ls.append(QSpinBox(self))
            self.time_ls[r].move(20 + 70 + 70 + 70, 165 + r * 28)
            self.time_ls[r].setValue(10)
            self.time_rs.append(QSpinBox(self))
            self.time_rs[r].move(20 + 70 + 70 + 70 + 55, 165 + r * 28)
            self.time_rs[r].setValue(55)
            self.time_lch_st.append(QTimeEdit(self))
            self.time_lch_st[r].setDisplayFormat("hh:mm")
            self.time_lch_st[r].setTime(QTime(15, 00))
            self.time_lch_st[r].move(20 + 70 + 70 + 70 + 55 + 55, 165 + r * 28)
            self.time_lch_ed.append(QTimeEdit(self))
            self.time_lch_ed[r].setDisplayFormat("hh:mm")
            self.time_lch_ed[r].setTime(QTime(15, 00))
            self.time_lch_ed[r].move(20 + 70 + 70 + 70 + 55 + 55 + 70, 165 + r * 28)
            self.lch_chk.append(QCheckBox("",self))
            self.lch_chk[r].move(20 + 70 + 70 + 70 + 55 + 55 + 70 + 55, 165 + r * 28)
            self.lch_chk[r].setChecked(True)

        self.lbl_bell = QLabel("벨 음량", self)
        self.lbl_bell.move(35, 400)
        self.bell_vol = QDial(self)
        self.bell_vol.move(5, 410)
        self.bell_vol.setValue(50)
        self.bell_vol.valueChanged.connect(self.ch_bell_vol)

        self.timer = QTimer()
        self.timer.timeout.connect(self.tChk)

        self.bell = QSoundEffect()
        self.bell.setSource(QUrl.fromLocalFile('sound.mp3'))

        self.show()
        self.timeStart()

    def ch_bell_vol(self):
        self.bell.setVolume((self.bell_vol.value() / 100))

    def timeStart(self):

        self.lblTitle.setText("타임벨 작동중")
        self.timer.start(1000)

    def timeStop(self):
        self.timer.stop()
        self.lblTitle.setText("타임벨 정지중")
        self.lblNow.setText("")

    def tChk(self):
        t = time.localtime()
        self.lblNow.setText("{}:{}:{}".format(t.tm_hour, str(t.tm_min).zfill(2), str(t.tm_sec).zfill(2)))
        w = t.tm_wday + 1

        if self.day_chk[w].isChecked() and self.time_st[w].time().hour() <= t.tm_hour and \
            self.time_ed[w].time().hour() > t.tm_hour and t.tm_sec == 0 and \
                (t.tm_min == self.time_ls[w].value() or t.tm_min == self.time_rs[w].value()):
            if self.lch_chk[w].isChecked() and self.time_lch_st[w].time().hour() <= t.tm_hour and \
                self.time_lch_ed[w].time().hour() > t.tm_hour:
                return

            self.play()

    def play(self):
        self.bell.play()
app = QApplication([])
ex = Exam()
sys.exit(app.exec_())
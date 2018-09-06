"""
PyQt5(16. 웹캠 움직임감지)
"""

import sys, cv2, numpy, time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Exam(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):


        self.cpt = cv2.VideoCapture(0)
        self.fps = 24
        self.sens = 300
        _, self.img_o = self.cpt.read()
        self.img_o = cv2.cvtColor(self.img_o, cv2.COLOR_RGB2GRAY)
        cv2.imwrite('Image.jpg', self.img_o)

        self.cnt = 0
        self.frame = QLabel(self)
        self.frame.resize(640, 480)
        self.frame.setScaledContents(True)
        self.frame.move(5, 5)

        self.btn_on = QPushButton("켜기", self)
        self.btn_on.resize(100, 25)
        self.btn_on.move(5, 490)
        self.btn_on.clicked.connect(self.start)

        self.btn_off = QPushButton("끄기", self)
        self.btn_off.resize(100, 25)
        self.btn_off.move(110, 490)
        self.btn_off.clicked.connect(self.stop)


        self.prt = QLabel(self)
        self.prt.resize(200, 25)
        self.prt.move(215, 490)

        self.sldr = QSlider(Qt.Horizontal, self)
        self.sldr.resize(100, 25)
        self.sldr.move(415, 490)
        self.sldr.setMinimum(1)
        self.sldr.setMaximum(30)
        self.sldr.setValue(24)
        self.sldr.valueChanged.connect(self.setFps)

        self.sldr1 = QSlider(Qt.Horizontal, self)
        self.sldr1.resize(100, 25)
        self.sldr1.move(520, 490)
        self.sldr1.setMinimum(50)
        self.sldr1.setMaximum(500)
        self.sldr1.setValue(300)
        self.sldr1.valueChanged.connect(self.setSens)

        self.setGeometry(500, 250, 650, 540)
        self.show()

    def setFps(self):
        self.fps = self.sldr.value()
        self.prt.setText("FPS {} 로 조젇!".format(str(self.fps)))
        self.timer.stop()
        self.timer.start(1000. / self.fps)


    def setSens(self):
        self.sens = self.sldr1.value()
        self.prt.setText("감도 {} 로 조정!".format(str(self.sens)))

    def nextFrameSlot(self):

        _, cam = self.cpt.read()
        cam = cv2.cvtColor(cam, cv2.COLOR_BGR2RGB)
        cam = cv2.flip(cam, 0)
        self.img_p = cv2.cvtColor(cam, cv2.COLOR_RGB2GRAY)
        cv2.imwrite('Image.jpg', self.img_p)
        self.compare(self.img_o, self.img_p)
        self.img_o = self.img_p.copy()
        img = QImage(cam, cam.shape[1], cam.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.frame.setPixmap(pix)

    def compare(self, img_o, img_p):
        err = numpy.sum((img_o.astype("float") - img_p.astype("float")) **2)
        err /= float(img_o.shape[0] * img_p.shape[1])

        if(err >= self.sens):
            t = time.localtime()
            self.prt.setText("{}-{}-{} {}:{}:{} 움직임 감지!".format(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec))


    def start(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)
        self.timer.start(1000. / self.fps)

    def stop(self):

        self.frame.setPixmap(QPixmap.fromImage(QImage()))
        self.timer.stop()

app = QApplication([])
ex = Exam()
sys.exit(app.exec_())
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDateTime, QDate, QTime, Qt






datetime = QDateTime.currentDateTime()


print("Local Date And Time IS {}".format(datetime.toString(Qt.DefaultLocaleLongDate)))
print("Universal Date And Time IS {}".format(datetime.toUTC().toString()))
print("The Offset From UTC IS {0} : Seconds ".format(datetime.offsetFromUtc()))




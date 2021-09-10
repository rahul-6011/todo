from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from panel import Ui_MainWindow
import os
from datetime import date
import calendar


class Root(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()

        self.ui.addtask.setPlaceholderText("Add a Task")

        self.ui.nameuser.setText(os.getlogin())
        self.ui.profile.setText(str(os.getlogin())[0])
        self.ui.nameuser2.setText(os.getlogin())
        self.ui.profile2.setText(str(os.getlogin())[0])

        date_full = str(date.today())
        mounth = calendar.month_name[int(date_full[5:7])]
        day = date.today().strftime("%A")

        self.ui.date.setText('%s, %s %s' % (day, mounth, date_full[8:]))
        self.ui.date2.setText('%s, %s %s' % (day, mounth, date_full[8:]))

    def mousePressEvent(self, evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):

        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    root = Root()
    sys.exit(app.exec_())

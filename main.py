from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from panel import Ui_MainWindow
import os
from datetime import date
import calendar
import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS tasks(
            task text,
            number integer
         )''')
conn.commit()

number_task = int()


class Root(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()

        self.ui.addtask.setPlaceholderText("Add a Task")
        self.ui.addtask_3.setPlaceholderText("Add a Task")

        self.ui.nameuser.setText(os.getlogin())
        self.ui.profile.setText(str(os.getlogin())[0])
        self.ui.nameuser2.setText(os.getlogin())
        self.ui.profile2.setText(str(os.getlogin())[0])

        date_full = str(date.today())
        mounth = calendar.month_name[int(date_full[5:7])]
        day = date.today().strftime("%A")

        self.ui.date.setText('%s, %s %s' % (day, mounth, date_full[8:]))
        self.ui.date2.setText('%s, %s %s' % (day, mounth, date_full[8:]))

        self.ui.submit.clicked.connect(self.submit)
        self.ui.submit_2.clicked.connect(self.submit2)

    def mousePressEvent(self, evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):

        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def submit(self):
        global number_task
        text = self.ui.addtask.text()
        self.ui.addtask.clear()
        if len(text) == 0:
            self.ui.addtask.setPlaceholderText("Please type a Task")
        else:
            number_task += 1
            self.add_task(number_task, text)

    def submit2(self):
        global number_task
        text = self.ui.addtask_3.text()
        self.ui.addtask_3.clear()
        if len(text) == 0:
            self.ui.addtask_3.setPlaceholderText("Please type a Task")
        else:
            number_task += 1
            self.add_task(number_task, text)

    def add_task(self, num, txt):
        global c
        global conn

        if num <= 8:
            new_data = ("""INSERT INTO tasks(task, number) VALUES ('{}',{});""".format(str(txt), int(num)))
            c.execute(new_data)
            conn.commit()

        tasks = c.execute('SELECT * FROM tasks')
        count = 0
        for row in tasks:
            count += 1
            txt = row[0]
            if count == 1:
                self.ui.stackedWidget.setCurrentWidget(self.ui.day_task)

                self.ui.task1.setStyleSheet("background-color: rgb(255, 213, 246, 150);\n"
                                            "color: rgb(70, 70, 70);\n"
                                            "border-radius: 7px;")
                self.ui.task1.setText(txt)
                self.ui.sub1.setStyleSheet("background-color: none;\n""color: rgb(127, 127, 127);\n")

            if count == 2:
                self.ui.task2.setStyleSheet("background-color: rgb(255, 213, 246, 150);\n"
                                            "color: rgb(70, 70, 70);\n"
                                            "border-radius: 7px;")
                self.ui.task2.setText(txt)

                self.ui.sub2.setStyleSheet("background-color: none;\n""color: rgb(127, 127, 127);\n")
            if count == 3:
                self.ui.task3.setStyleSheet("background-color: rgb(255, 213, 246, 150);\n"
                                            "color: rgb(70, 70, 70);\n"
                                            "border-radius: 7px;")
                self.ui.task3.setText(txt)

                self.ui.sub3.setStyleSheet("background-color: none;\n""color: rgb(127, 127, 127);\n")
            if count == 4:
                self.ui.task4.setStyleSheet("background-color: rgb(255, 213, 246, 150);\n"
                                            "color: rgb(70, 70, 70);\n"
                                            "border-radius: 7px;")
                self.ui.task4.setText(txt)

                self.ui.sub4.setStyleSheet("background-color: none;\n""color: rgb(127, 127, 127);\n")
            if count == 5:
                self.ui.task5.setStyleSheet("background-color: rgb(255, 213, 246, 150);\n"
                                            "color: rgb(70, 70, 70);\n"
                                            "border-radius: 7px;")
                self.ui.task5.setText(txt)

                self.ui.sub5.setStyleSheet("background-color: none;\n""color: rgb(127, 127, 127);\n")
            if count == 6:
                self.ui.task6.setStyleSheet("background-color: rgb(255, 213, 246, 180);\n"
                                            "color: rgb(70, 70, 70);\n"
                                            "border-radius: 7px;")
                self.ui.task6.setText(txt)

                self.ui.sub6.setStyleSheet("background-color: none;\n""color: rgb(127, 127, 127);\n")
            if count == 7:
                self.ui.task7.setStyleSheet("background-color: rgb(255, 213, 246, 180);\n"
                                            "color: rgb(70, 70, 70);\n"
                                            "border-radius: 7px;")
                self.ui.task7.setText(txt)

                self.ui.sub7.setStyleSheet("background-color: none;\n""color: rgb(127, 127, 127);\n")
            if count == 8:
                self.ui.task8.setStyleSheet("background-color: rgb(255, 213, 246, 180);\n"
                                            "color: rgb(70, 70, 70);\n"
                                            "border-radius: 7px;")
                self.ui.task8.setText(txt)

                self.ui.sub8.setStyleSheet("background-color: none;\n""color: rgb(127, 127, 127);\n")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    root = Root()
    sys.exit(app.exec_())

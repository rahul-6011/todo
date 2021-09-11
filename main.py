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
number = 0


class Root(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()

        self.set_task()

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

        # del task
        self.ui.delete1.clicked.connect(self.remove_task1)
        self.ui.delete2.clicked.connect(self.remove_task2)
        self.ui.delete3.clicked.connect(self.remove_task3)
        self.ui.delete4.clicked.connect(self.remove_task4)
        self.ui.delete5.clicked.connect(self.remove_task5)
        self.ui.delete6.clicked.connect(self.remove_task6)
        self.ui.delete7.clicked.connect(self.remove_task7)
        self.ui.delete8.clicked.connect(self.remove_task8)

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
        self.set_task()

    def set_task(self):
        global number
        number = 0
        tasks = c.execute('SELECT * FROM tasks')
        for temp in tasks:
            number += 1

        if number == 0:
            self.ui.stackedWidget.setCurrentWidget(self.ui.day)

        count = 0
        tasks = c.execute('SELECT * FROM tasks')
        for row in tasks:
            count += 1
            txt = row[0]
            if count == 1:
                self.ui.stackedWidget.setCurrentWidget(self.ui.day_task)
                self.ui.task1.show()
                self.ui.task1.setText(txt)
                self.ui.sub1.show()
                self.ui.delete1.show()
            if count == 2:
                self.ui.task2.show()
                self.ui.task2.setText(txt)
                self.ui.sub2.show()
                self.ui.delete2.show()
            if count == 3:
                self.ui.task3.show()
                self.ui.task3.setText(txt)
                self.ui.sub3.show()
                self.ui.delete3.show()
            if count == 4:
                self.ui.task4.show()
                self.ui.task4.setText(txt)
                self.ui.sub4.show()
                self.ui.delete4.show()
            if count == 5:
                self.ui.task5.show()
                self.ui.task5.setText(txt)
                self.ui.sub5.show()
                self.ui.delete5.show()
            if count == 6:
                self.ui.task6.show()
                self.ui.task6.setText(txt)
                self.ui.sub6.show()
                self.ui.delete6.show()
            if count == 7:
                self.ui.task7.show()
                self.ui.task7.setText(txt)
                self.ui.sub7.show()
                self.ui.delete7.show()
            if count == 8:
                self.ui.task8.show()
                self.ui.task8.setText(txt)
                self.ui.sub8.show()
                self.ui.delete8.show()

    def remove_task1(self):
        global c
        global conn
        global number
        task = self.ui.task1.text()
        c.execute(f'DELETE FROM TASKS WHERE task = "{task}"')
        conn.commit()
        self.ui.task1.clear()
        self.ui.task2.clear()
        self.ui.task3.clear()
        self.ui.task4.clear()
        self.ui.task5.clear()
        self.ui.task6.clear()
        self.ui.task7.clear()
        self.ui.task8.clear()
        if number == 8:
            self.ui.task8.hide()
            self.ui.sub8.hide()
            self.ui.delete8.hide()
        elif number == 7:
            self.ui.task7.hide()
            self.ui.sub7.hide()
            self.ui.delete7.hide()
        elif number == 6:
            self.ui.task6.hide()
            self.ui.sub6.hide()
            self.ui.delete6.hide()
        elif number == 5:
            self.ui.task5.hide()
            self.ui.sub5.hide()
            self.ui.delete5.hide()
        elif number == 4:
            self.ui.task4.hide()
            self.ui.sub4.hide()
            self.ui.delete4.hide()
        elif number == 3:
            self.ui.task3.hide()
            self.ui.sub3.hide()
            self.ui.delete3.hide()
        elif number == 2:
            self.ui.task2.hide()
            self.ui.sub2.hide()
            self.ui.delete2.hide()
        elif number == 1:
            self.ui.task1.hide()
            self.ui.sub1.hide()
            self.ui.delete1.hide()

        self.set_task()

    def remove_task2(self):
        global c
        global conn
        global number
        task = self.ui.task2.text()
        c.execute(f'DELETE FROM TASKS WHERE task = "{task}"')
        conn.commit()
        self.ui.task1.clear()
        self.ui.task2.clear()
        self.ui.task3.clear()
        self.ui.task4.clear()
        self.ui.task5.clear()
        self.ui.task6.clear()
        self.ui.task7.clear()
        self.ui.task8.clear()

        if number == 8:
            self.ui.task8.hide()
            self.ui.sub8.hide()
            self.ui.delete8.hide()
        elif number == 7:
            self.ui.task7.hide()
            self.ui.sub7.hide()
            self.ui.delete7.hide()
        elif number == 6:
            self.ui.task6.hide()
            self.ui.sub6.hide()
            self.ui.delete6.hide()
        elif number == 5:
            self.ui.task5.hide()
            self.ui.sub5.hide()
            self.ui.delete5.hide()
        elif number == 4:
            self.ui.task4.hide()
            self.ui.sub4.hide()
            self.ui.delete4.hide()
        elif number == 3:
            self.ui.task3.hide()
            self.ui.sub3.hide()
            self.ui.delete3.hide()
        elif number == 2:
            self.ui.task2.hide()
            self.ui.sub2.hide()
            self.ui.delete2.hide()
        elif number == 1:
            self.ui.task1.hide()
            self.ui.sub1.hide()
            self.ui.delete1.hide()

        self.set_task()

    def remove_task3(self):
        global c
        global conn
        global number
        task = self.ui.task3.text()
        c.execute(f'DELETE FROM TASKS WHERE task = "{task}"')
        conn.commit()
        self.ui.task1.clear()
        self.ui.task2.clear()
        self.ui.task3.clear()
        self.ui.task4.clear()
        self.ui.task5.clear()
        self.ui.task6.clear()
        self.ui.task7.clear()
        self.ui.task8.clear()

        if number == 8:
            self.ui.task8.hide()
            self.ui.sub8.hide()
            self.ui.delete8.hide()
        elif number == 7:
            self.ui.task7.hide()
            self.ui.sub7.hide()
            self.ui.delete7.hide()
        elif number == 6:
            self.ui.task6.hide()
            self.ui.sub6.hide()
            self.ui.delete6.hide()
        elif number == 5:
            self.ui.task5.hide()
            self.ui.sub5.hide()
            self.ui.delete5.hide()
        elif number == 4:
            self.ui.task4.hide()
            self.ui.sub4.hide()
            self.ui.delete4.hide()
        elif number == 3:
            self.ui.task3.hide()
            self.ui.sub3.hide()
            self.ui.delete3.hide()
        elif number == 2:
            self.ui.task2.hide()
            self.ui.sub2.hide()
            self.ui.delete2.hide()
        elif number == 1:
            self.ui.task1.hide()
            self.ui.sub1.hide()
            self.ui.delete1.hide()

        self.set_task()

    def remove_task4(self):
        global c
        global conn
        global number
        task = self.ui.task4.text()
        c.execute(f'DELETE FROM TASKS WHERE task = "{task}"')
        conn.commit()
        self.ui.task1.clear()
        self.ui.task2.clear()
        self.ui.task3.clear()
        self.ui.task4.clear()
        self.ui.task5.clear()
        self.ui.task6.clear()
        self.ui.task7.clear()
        self.ui.task8.clear()

        if number == 8:
            self.ui.task8.hide()
            self.ui.sub8.hide()
            self.ui.delete8.hide()
        elif number == 7:
            self.ui.task7.hide()
            self.ui.sub7.hide()
            self.ui.delete7.hide()
        elif number == 6:
            self.ui.task6.hide()
            self.ui.sub6.hide()
            self.ui.delete6.hide()
        elif number == 5:
            self.ui.task5.hide()
            self.ui.sub5.hide()
            self.ui.delete5.hide()
        elif number == 4:
            self.ui.task4.hide()
            self.ui.sub4.hide()
            self.ui.delete4.hide()
        elif number == 3:
            self.ui.task3.hide()
            self.ui.sub3.hide()
            self.ui.delete3.hide()
        elif number == 2:
            self.ui.task2.hide()
            self.ui.sub2.hide()
            self.ui.delete2.hide()
        elif number == 1:
            self.ui.task1.hide()
            self.ui.sub1.hide()
            self.ui.delete1.hide()

        self.set_task()

    def remove_task5(self):
        global c
        global conn
        global number
        task = self.ui.task5.text()
        c.execute(f'DELETE FROM TASKS WHERE task = "{task}"')
        conn.commit()
        self.ui.task1.clear()
        self.ui.task2.clear()
        self.ui.task3.clear()
        self.ui.task4.clear()
        self.ui.task5.clear()
        self.ui.task6.clear()
        self.ui.task7.clear()
        self.ui.task8.clear()

        if number == 8:
            self.ui.task8.hide()
            self.ui.sub8.hide()
            self.ui.delete8.hide()
        elif number == 7:
            self.ui.task7.hide()
            self.ui.sub7.hide()
            self.ui.delete7.hide()
        elif number == 6:
            self.ui.task6.hide()
            self.ui.sub6.hide()
            self.ui.delete6.hide()
        elif number == 5:
            self.ui.task5.hide()
            self.ui.sub5.hide()
            self.ui.delete5.hide()
        elif number == 4:
            self.ui.task4.hide()
            self.ui.sub4.hide()
            self.ui.delete4.hide()
        elif number == 3:
            self.ui.task3.hide()
            self.ui.sub3.hide()
            self.ui.delete3.hide()
        elif number == 2:
            self.ui.task2.hide()
            self.ui.sub2.hide()
            self.ui.delete2.hide()
        elif number == 1:
            self.ui.task1.hide()
            self.ui.sub1.hide()
            self.ui.delete1.hide()

        self.set_task()

    def remove_task6(self):
        global c
        global conn
        global number
        task = self.ui.task6.text()
        c.execute(f'DELETE FROM TASKS WHERE task = "{task}"')
        conn.commit()
        self.ui.task1.clear()
        self.ui.task2.clear()
        self.ui.task3.clear()
        self.ui.task4.clear()
        self.ui.task5.clear()
        self.ui.task6.clear()
        self.ui.task7.clear()
        self.ui.task8.clear()

        if number == 8:
            self.ui.task8.hide()
            self.ui.sub8.hide()
            self.ui.delete8.hide()
        elif number == 7:
            self.ui.task7.hide()
            self.ui.sub7.hide()
            self.ui.delete7.hide()
        elif number == 6:
            self.ui.task6.hide()
            self.ui.sub6.hide()
            self.ui.delete6.hide()
        elif number == 5:
            self.ui.task5.hide()
            self.ui.sub5.hide()
            self.ui.delete5.hide()
        elif number == 4:
            self.ui.task4.hide()
            self.ui.sub4.hide()
            self.ui.delete4.hide()
        elif number == 3:
            self.ui.task3.hide()
            self.ui.sub3.hide()
            self.ui.delete3.hide()
        elif number == 2:
            self.ui.task2.hide()
            self.ui.sub2.hide()
            self.ui.delete2.hide()
        elif number == 1:
            self.ui.task1.hide()
            self.ui.sub1.hide()
            self.ui.delete1.hide()

        self.set_task()

    def remove_task7(self):
        global c
        global conn
        global number
        task = self.ui.task7.text()
        c.execute(f'DELETE FROM TASKS WHERE task = "{task}"')
        conn.commit()
        self.ui.task1.clear()
        self.ui.task2.clear()
        self.ui.task3.clear()
        self.ui.task4.clear()
        self.ui.task5.clear()
        self.ui.task6.clear()
        self.ui.task7.clear()
        self.ui.task8.clear()

        if number == 8:
            self.ui.task8.hide()
            self.ui.sub8.hide()
            self.ui.delete8.hide()
        elif number == 7:
            self.ui.task7.hide()
            self.ui.sub7.hide()
            self.ui.delete7.hide()
        elif number == 6:
            self.ui.task6.hide()
            self.ui.sub6.hide()
            self.ui.delete6.hide()
        elif number == 5:
            self.ui.task5.hide()
            self.ui.sub5.hide()
            self.ui.delete5.hide()
        elif number == 4:
            self.ui.task4.hide()
            self.ui.sub4.hide()
            self.ui.delete4.hide()
        elif number == 3:
            self.ui.task3.hide()
            self.ui.sub3.hide()
            self.ui.delete3.hide()
        elif number == 2:
            self.ui.task2.hide()
            self.ui.sub2.hide()
            self.ui.delete2.hide()
        elif number == 1:
            self.ui.task1.hide()
            self.ui.sub1.hide()
            self.ui.delete1.hide()

        self.set_task()

    def remove_task8(self):
        global c
        global conn
        global number
        task = self.ui.task8.text()
        c.execute(f'DELETE FROM TASKS WHERE task = "{task}"')
        conn.commit()
        self.ui.task1.clear()
        self.ui.task2.clear()
        self.ui.task3.clear()
        self.ui.task4.clear()
        self.ui.task5.clear()
        self.ui.task6.clear()
        self.ui.task7.clear()
        self.ui.task8.clear()

        if number == 8:
            self.ui.task8.hide()
            self.ui.sub8.hide()
            self.ui.delete8.hide()
        elif number == 7:
            self.ui.task7.hide()
            self.ui.sub7.hide()
            self.ui.delete7.hide()
        elif number == 6:
            self.ui.task6.hide()
            self.ui.sub6.hide()
            self.ui.delete6.hide()
        elif number == 5:
            self.ui.task5.hide()
            self.ui.sub5.hide()
            self.ui.delete5.hide()
        elif number == 4:
            self.ui.task4.hide()
            self.ui.sub4.hide()
            self.ui.delete4.hide()
        elif number == 3:
            self.ui.task3.hide()
            self.ui.sub3.hide()
            self.ui.delete3.hide()
        elif number == 2:
            self.ui.task2.hide()
            self.ui.sub2.hide()
            self.ui.delete2.hide()
        elif number == 1:
            self.ui.task1.hide()
            self.ui.sub1.hide()
            self.ui.delete1.hide()

        self.set_task()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    root = Root()
    sys.exit(app.exec_())

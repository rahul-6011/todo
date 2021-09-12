from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from panel import Ui_MainWindow
import os
from datetime import date
import calendar
import sqlite3
from pygame import mixer

date_full = str(date.today()).split('-')
date_name = 'date'+date_full[0]+date_full[1]+date_full[2]

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute(f'''CREATE TABLE IF NOT EXISTS {date_name}(
            task text,
            number integer,
            status integer
         )''')
conn.commit()

page_time = 0
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

        timer = QTimer(self)
        timer.timeout.connect(self.timer)
        timer.start(1000)

        self.ui.addtask.setPlaceholderText("Add a Task")
        self.ui.addtask_3.setPlaceholderText("Add a Task")

        self.ui.nameuser.setText(os.getlogin())
        self.ui.profile.setText(str(os.getlogin())[0])
        self.ui.nameuser2.setText(os.getlogin())
        self.ui.profile2.setText(str(os.getlogin())[0])
        self.ui.nameuser2_2.setText(os.getlogin())
        self.ui.profile2_2.setText(str(os.getlogin())[0])

        self.ui.submit.clicked.connect(self.submit)
        self.ui.submit_2.clicked.connect(self.submit2)

        self.ui.timer1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer1.clicked.connect(self.page_clock)
        self.ui.timer2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer2.clicked.connect(self.page_clock)
        self.ui.timer3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer3.clicked.connect(self.page_clock)
        self.ui.timer4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer4.clicked.connect(self.page_clock)
        self.ui.timer5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer5.clicked.connect(self.page_clock)
        self.ui.timer6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer6.clicked.connect(self.page_clock)
        self.ui.timer7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer7.clicked.connect(self.page_clock)
        self.ui.timer8.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer8.clicked.connect(self.page_clock)
        self.ui.cancel_time.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.day_task))
        self.ui.cancel_time.clicked.connect(self.page_clock_cancel)
        self.ui.sub_time.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.day_task))
        self.ui.sub_time.clicked.connect(self.set_clock)
        self.ui.ok_clock.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.day_task))
        self.ui.ok_clock.clicked.connect(self.stop_clock)
        self.ui.comp1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.completed))
        self.ui.comp1.clicked.connect(self.page_clock)
        self.ui.my_day3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.day_task))
        self.ui.my_day3.clicked.connect(self.page_clock_cancel)
        self.ui.comp2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.completed))
        self.ui.comp2.clicked.connect(self.page_clock)

        # del task
        self.ui.delete1.clicked.connect(self.remove_task1)
        self.ui.delete2.clicked.connect(self.remove_task2)
        self.ui.delete3.clicked.connect(self.remove_task3)
        self.ui.delete4.clicked.connect(self.remove_task4)
        self.ui.delete5.clicked.connect(self.remove_task5)
        self.ui.delete6.clicked.connect(self.remove_task6)
        self.ui.delete7.clicked.connect(self.remove_task7)
        self.ui.delete8.clicked.connect(self.remove_task8)

        # Completed task
        self.ui.sub1.clicked.connect(self.sub_task1)
        self.ui.sub2.clicked.connect(self.sub_task2)
        self.ui.sub3.clicked.connect(self.sub_task3)
        self.ui.sub4.clicked.connect(self.sub_task4)
        self.ui.sub5.clicked.connect(self.sub_task5)
        self.ui.sub6.clicked.connect(self.sub_task6)
        self.ui.sub7.clicked.connect(self.sub_task7)
        self.ui.sub8.clicked.connect(self.sub_task8)

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
        global date_name

        if num <= 8:
            new_data = ("""INSERT INTO {}(task, number, status) VALUES ('{}',{}, {});""".format(date_name, str(txt), int(num), 0))
            c.execute(new_data)
            conn.commit()
        self.set_task()

    def set_task(self):
        global number
        global date_name
        global page_time
        number = 0
        tasks = c.execute(f'SELECT * FROM {date_name}')
        for temp in tasks:
            if temp[2] == 0:
                number += 1

        if number == 0 and page_time != 1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.day)

        count = 0
        tasks = c.execute(f'SELECT * FROM {date_name}')
        for row in tasks:
            if int(row[2]) == 0:
                count += 1
                txt = row[0]
                if count == 1:
                    if page_time != 1:
                        self.ui.stackedWidget.setCurrentWidget(self.ui.day_task)
                    self.ui.task1.show()
                    self.ui.task1.setText(txt)
                    self.ui.sub1.show()
                    self.ui.delete1.show()
                    self.ui.timer1.show()
                if count == 2:
                    self.ui.task2.show()
                    self.ui.task2.setText(txt)
                    self.ui.sub2.show()
                    self.ui.delete2.show()
                    self.ui.timer2.show()
                if count == 3:
                    self.ui.task3.show()
                    self.ui.task3.setText(txt)
                    self.ui.sub3.show()
                    self.ui.delete3.show()
                    self.ui.timer3.show()
                if count == 4:
                    self.ui.task4.show()
                    self.ui.task4.setText(txt)
                    self.ui.sub4.show()
                    self.ui.delete4.show()
                    self.ui.timer4.show()
                if count == 5:
                    self.ui.task5.show()
                    self.ui.task5.setText(txt)
                    self.ui.sub5.show()
                    self.ui.delete5.show()
                    self.ui.timer5.show()
                if count == 6:
                    self.ui.task6.show()
                    self.ui.task6.setText(txt)
                    self.ui.sub6.show()
                    self.ui.delete6.show()
                    self.ui.timer6.show()
                if count == 7:
                    self.ui.task7.show()
                    self.ui.task7.setText(txt)
                    self.ui.sub7.show()
                    self.ui.delete7.show()
                    self.ui.timer7.show()
                if count == 8:
                    self.ui.task8.show()
                    self.ui.task8.setText(txt)
                    self.ui.sub8.show()
                    self.ui.delete8.show()
                    self.ui.timer8.show()

    def set_completed(self):
        global date_name
        count = 0
        tasks = c.execute(f'SELECT * FROM {date_name}')
        for row in tasks:
            if int(row[2]) == 1:
                count += 1
                txt = row[0]
                if count == 1:
                    self.ui.com1.show()
                    self.ui.com1.setText(txt)
                if count == 2:
                    self.ui.com2.show()
                    self.ui.com2.setText(txt)
                if count == 3:
                    self.ui.com3.show()
                    self.ui.com3.setText(txt)
                if count == 4:
                    self.ui.com4.show()
                    self.ui.com4.setText(txt)
                if count == 5:
                    self.ui.com5.show()
                    self.ui.com5.setText(txt)
                if count == 6:
                    self.ui.com6.show()
                    self.ui.com6.setText(txt)
                if count == 7:
                    self.ui.com7.show()
                    self.ui.com7.setText(txt)
                if count == 8:
                    self.ui.com8.show()
                    self.ui.com8.setText(txt)

    def remove_task1(self):
        global c
        global conn
        global number
        global date_name
        task = self.ui.task1.text()
        c.execute(f'DELETE FROM {date_name} WHERE task = "{task}"')
        conn.commit()
        self.remover(number)
        self.set_task()

    def remove_task2(self):
        global c
        global conn
        global number
        global date_name
        task = self.ui.task2.text()
        c.execute(f'DELETE FROM {date_name} WHERE task = "{task}"')
        conn.commit()
        self.remover(number)
        self.set_task()

    def remove_task3(self):
        global c
        global conn
        global number
        global date_name
        task = self.ui.task3.text()
        c.execute(f'DELETE FROM {date_name} WHERE task = "{task}"')
        conn.commit()
        self.remover(number)
        self.set_task()

    def remove_task4(self):
        global c
        global conn
        global number
        global date_name
        task = self.ui.task4.text()
        c.execute(f'DELETE FROM {date_name} WHERE task = "{task}"')
        conn.commit()
        self.remover(number)
        self.set_task()

    def remove_task5(self):
        global c
        global conn
        global number
        global date_name
        task = self.ui.task5.text()
        c.execute(f'DELETE FROM {date_name} WHERE task = "{task}"')
        conn.commit()
        self.remover(number)
        self.set_task()

    def remove_task6(self):
        global c
        global conn
        global number
        global date_name
        task = self.ui.task6.text()
        c.execute(f'DELETE FROM {date_name} WHERE task = "{task}"')
        conn.commit()
        self.remover(number)
        self.set_task()

    def remove_task7(self):
        global c
        global conn
        global number
        global date_name
        task = self.ui.task7.text()
        c.execute(f'DELETE FROM {date_name} WHERE task = "{task}"')
        conn.commit()
        self.remover(number)
        self.set_task()

    def remove_task8(self):
        global c
        global conn
        global number
        global date_name
        task = self.ui.task8.text()
        c.execute(f'DELETE FROM {date_name} WHERE task = "{task}"')
        conn.commit()
        self.remover(number)
        self.set_task()

    def remover(self, num):
        self.ui.task1.clear()
        self.ui.task2.clear()
        self.ui.task3.clear()
        self.ui.task4.clear()
        self.ui.task5.clear()
        self.ui.task6.clear()
        self.ui.task7.clear()
        self.ui.task8.clear()
        if num == 8:
            self.ui.task8.hide()
            self.ui.sub8.hide()
            self.ui.delete8.hide()
            self.ui.timer8.hide()
        elif num == 7:
            self.ui.task7.hide()
            self.ui.sub7.hide()
            self.ui.delete7.hide()
            self.ui.timer7.hide()
        elif num == 6:
            self.ui.task6.hide()
            self.ui.sub6.hide()
            self.ui.delete6.hide()
            self.ui.timer6.hide()
        elif num == 5:
            self.ui.task5.hide()
            self.ui.sub5.hide()
            self.ui.delete5.hide()
            self.ui.timer5.hide()
        elif num == 4:
            self.ui.task4.hide()
            self.ui.sub4.hide()
            self.ui.delete4.hide()
            self.ui.timer4.hide()
        elif num == 3:
            self.ui.task3.hide()
            self.ui.sub3.hide()
            self.ui.delete3.hide()
            self.ui.timer3.hide()
        elif num == 2:
            self.ui.task2.hide()
            self.ui.sub2.hide()
            self.ui.delete2.hide()
            self.ui.timer2.hide()
        elif num == 1:
            self.ui.task1.hide()
            self.ui.sub1.hide()
            self.ui.delete1.hide()
            self.ui.timer1.hide()

    def page_clock(self):
        global page_time
        page_time = 1
        self.ui.hh.clearFocus()
        self.ui.hh.setPlaceholderText("00")
        self.ui.mm.setPlaceholderText("00")
        self.ui.ss.setPlaceholderText("00")

    def page_clock_cancel(self):
        global page_time
        page_time = 0

    def timer(self):
        global c
        global conn
        global date_name
        global date_full

        # get time
        currentTime = QTime.currentTime()
        display_text = currentTime.toString('hh:mm:ss')
        self.ui.now_time.setText(display_text)

        # set date
        date_full2 = str(date.today())
        mounth = calendar.month_name[int(date_full2[5:7])]
        day = date.today().strftime("%A")

        self.ui.date.setText('%s, %s %s' % (day, mounth, date_full2[8:]))
        self.ui.date2.setText('%s, %s %s' % (day, mounth, date_full2[8:]))
        self.ui.date3.setText('%s, %s %s' % (day, mounth, date_full2[8:]))

        # set date - database
        date_full = str(date.today()).split('-')
        date_name = 'date' + date_full[0] + date_full[1] + date_full[2]

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute(f'''CREATE TABLE IF NOT EXISTS {date_name}(
                    task text,
                    number integer,
                    status integer
                 )''')
        conn.commit()

        # Update task
        self.set_task()
        self.set_completed()

        c.execute(f'''CREATE TABLE IF NOT EXISTS {date_name+'time'}(
                    time text
                 )''')
        conn.commit()

        # clock
        clocks = c.execute(f'SELECT * FROM {date_name+"time"}')
        for row in clocks:
            if str(list(row)[0]) == str(display_text):
                mixer.init()
                mixer.music.load('alarms/alarm1.mp3')
                mixer.music.play()
                self.ui.stackedWidget.setCurrentWidget(self.ui.stop_timer)
                c.execute(f'DELETE FROM {date_name+"time"} WHERE time = "{display_text}"')
                conn.commit()

    def set_clock(self):
        global c
        global conn
        global date_name

        clock = str(self.ui.hh.text()+':'+self.ui.mm.text()+':'+self.ui.ss.text())
        self.ui.hh.clear()
        self.ui.mm.clear()
        self.ui.ss.clear()
        new_data = ("""INSERT INTO {}(time) VALUES ('{}');""".format(date_name+'time', clock))
        c.execute(new_data)
        conn.commit()

    def stop_clock(self):
        mixer.music.stop()

    def sub_task1(self):
        task = self.ui.task1.text()
        self.sub_tasks(task)

    def sub_task2(self):
        task = self.ui.task2.text()
        self.sub_tasks(task)

    def sub_task3(self):
        task = self.ui.task3.text()
        self.sub_tasks(task)

    def sub_task4(self):
        task = self.ui.task4.text()
        self.sub_tasks(task)

    def sub_task5(self):
        task = self.ui.task5.text()
        self.sub_tasks(task)

    def sub_task6(self):
        task = self.ui.task6.text()
        self.sub_tasks(task)

    def sub_task7(self):
        task = self.ui.task7.text()
        self.sub_tasks(task)

    def sub_task8(self):
        task = self.ui.task8.text()
        self.sub_tasks(task)

    def sub_tasks(self, task):
        global c
        global conn
        global date_name
        global number
        num = 1
        sql_update_query = """Update {} set status = {} where task = '{}'""".format(date_name, num, str(task))
        c.execute(sql_update_query)
        conn.commit()
        self.remover(number)
        self.set_task()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    root = Root()
    sys.exit(app.exec_())

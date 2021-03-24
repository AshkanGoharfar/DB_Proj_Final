import pymysql
import hashlib
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import time
from datetime import datetime
import pandas as pd


import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

db = pymysql.connect(host="127.0.0.1", user="ashkan", passwd="password", database="db_final_proj", port=3305)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Login or Create Account"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        buttonWindow1 = QPushButton('Login', self)
        buttonWindow1.move(100, 100)
        buttonWindow1.clicked.connect(self.buttonWindow1_onClick)
        self.lineEdit1 = QLineEdit("Username,Password", self)
        self.lineEdit1.setGeometry(250, 100, 400, 30)
        # execute SQL query using execute() method.

        buttonWindow2 = QPushButton('Create an account', self)
        buttonWindow2.setGeometry(70, 200, 150, 30)
        buttonWindow2.clicked.connect(self.buttonWindow2_onClick)
        # inputs are like this: p_id, username, password, created_day, budget, first_name, last_name, phone, address, user_type , uni_job
        self.lineEdit2 = QLineEdit("2,asad,aaa,10-02-2021,1000,A,sdsd,09121010101,Iran-Teran,Instructor,AmirKabir",
                                   self)
        self.lineEdit2.setGeometry(250, 200, 400, 30)
        self.show()

    @pyqtSlot()
    def buttonWindow1_onClick(self):
        self.statusBar().showMessage('The first page')
        input = self.lineEdit1.text()
        user_pass = input.split(',')
        user_pass[1] = hashlib.md5(user_pass[1].encode()).hexdigest()
        print(user_pass)
        # execute SQL query using execute() method.
        query = input
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        query_split = query.split(",")
        q = "select * from " + "account_system_info" + " where 1"
        try:
            cursor.execute(q)
            df = list(cursor.fetchall())
            # print(list(df))
        except pymysql.err.ProgrammingError as err:
            # print(err)
            self.statusBar().showMessage(err)

        # print(df.col)
        print(df[1], df[2])
        all_user_pass = {}
        for item in df:
            all_user_pass[item[1]] = {'id': item[1], 'pass': item[2]}

        if user_pass[0] not in all_user_pass:
            self.cams = Window1("Wrong Username !!!!")
            self.cams.show()
            self.close()
        else:
            if all_user_pass[user_pass[0]]['pass'] != user_pass[1]:
                self.cams = Window3("Wrong Password !!!!")
                self.cams.show()
                self.close()
            else:
                self.cams = Window4('')
                self.cams.show()
                self.close()

    @pyqtSlot()
    def buttonWindow2_onClick(self):
        self.statusBar().showMessage('The second page')
        input = self.lineEdit2.text()
        user_pass = input.split(',')
        hashed_pass = hashlib.md5(user_pass[1].encode()).hexdigest()
        print('before: ')
        print(user_pass)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        q = "INSERT" + " INTO " + "account_system_info (p_id, username, password, created_day, budget, first_name, last_name, phone, address, user_type , uni_job)" + "VALUES ('43', 'ash', 'kkk', '08-03-2021', '5000', 'khkh', 'khjgkgkg', '09121010198', 'Iran-Teran-4', 'student', 'AmirKabir')"
        q2 = "VALUES ('3', 'bvr', 'ddd', '10-03-2021', '2000', 'naghi', 'wewe', '09121010101', 'Iran-Teran-1', 'student', 'AmirKabir')"
        try:
            # sql = "INSERT INTO " + "account_system_info (p_id, username, password, created_day, budget, first_name, last_name, phone, address, user_type , uni_job) VALUES (%d, %s, %s, %s,%d, %s, %s, %s, %s, %s, %s)"
            # sql = "INSERT INTO " + "account_system_info(p_id, username, password, created_day, budget, first_name, " \
            #                        "last_name, phone, address, user_type , uni_job)" + " VALUES (43, 'ash', 'kkk', " \
            #                                                                            "'08-03-2021', 5000, 'khkh', " \
            #                                                                            "'khjgkgkg', '09121010198', " \
            #                                                                            "'Iran-Teran-4', 'student', " \
            #                                                                            "'AmirKabir') "
            sql = "INSERT INTO " + "publisher(pub_id, pub_address, pub_website)" + " VALUES (10, 'Lenovo ThinkPad P71', 'www.')"
            # val = ('43', 'ash', 'kkk', '08-03-2021', '5000', 'khkh', 'khjgkgkg', '09121010198', 'Iran-Teran-4', 'student', 'AmirKabir')
            cursor.execute(sql)

            db.commit()
            # cursor.execute(q)
            # cursor.execute(q2)
            df = list(cursor.fetchall())
            print('Successfullyi')
            print(list(df))
        except pymysql.err.ProgrammingError as err:
            print(err)
            self.statusBar().showMessage(err)

        # print(df.col)
        print(df[1], df[2])

        self.cams = Window2(self.lineEdit2.text())
        self.cams.show()
        self.close()

    # @pyqtSlot()
    # def buttonWindow2_onClick(self):
    #     self.statusBar().showMessage("Switched to window 2")
    #     self.cams = Window2(self.lineEdit2.text())
    #     self.cams.show()
    #     self.close()


class Window1(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Wrong username')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))

        label1 = QLabel(value)
        self.button = QPushButton()
        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
        self.pushButton.setText('Last window')
        self.pushButton.clicked.connect(self.goMainWindow)
        layoutV.addWidget(self.pushButton)

        layoutH = QHBoxLayout()
        layoutH.addWidget(label1)
        layoutH.addWidget(self.button)
        layoutV.addLayout(layoutH)
        self.setLayout(layoutV)

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()


class Window3(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Wrong password !!')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))

        label1 = QLabel(value)
        self.button = QPushButton()
        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
        self.pushButton.setText('Last window')
        self.pushButton.clicked.connect(self.goMainWindow)
        layoutV.addWidget(self.pushButton)

        layoutH = QHBoxLayout()
        layoutH.addWidget(label1)
        layoutH.addWidget(self.button)
        layoutV.addLayout(layoutH)
        self.setLayout(layoutV)

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()


# class Window5(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.title = "Login or Create Account"
#         self.top = 100
#         self.left = 100
#         self.width = 680
#         self.height = 500
#         self.InitUI()
#
#     def InitUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.top, self.left, self.width, self.height)
#
#         buttonWindow1 = QPushButton('Login', self)
#         buttonWindow1.move(100, 100)
#         buttonWindow1.clicked.connect(self.buttonWindow1_onClick)
#         self.lineEdit1 = QLineEdit("Username,Password", self)
#         self.lineEdit1.setGeometry(250, 100, 400, 30)
#         # execute SQL query using execute() method.
#
#         buttonWindow2 = QPushButton('Create an account', self)
#         buttonWindow2.setGeometry(70, 200, 150, 30)
#         buttonWindow2.clicked.connect(self.buttonWindow2_onClick)
#         # inputs are like this: p_id, username, password, created_day, budget, first_name, last_name, phone, address, user_type , uni_job
#         self.lineEdit2 = QLineEdit("2,asad,aaa,10-02-2021,1000,A,sdsd,09121010101,Iran-Teran,Instructor,AmirKabir",
#                                    self)
#         self.lineEdit2.setGeometry(250, 200, 400, 30)
#         self.show()
#     #


class Window4(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Home Page')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.table = 'account_system_info'
        label1 = QLabel(value)
        self.button = QPushButton()
        layoutV = QVBoxLayout()
        self.pushButton = QPushButton('Last window', self)
        self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
        self.pushButton.setGeometry(0, 40, 30, 30)
        # self.pushButton.move(100, 100)
        self.pushButton.clicked.connect(self.goMainWindow)
        layoutV.addWidget(self.pushButton)

        buttonWindow1 = QPushButton('Show Table', self)
        buttonWindow1.move(100, 100)

        buttonWindow1.clicked.connect(self.buttonWindow3_onClick)
        self.lineEdit1 = QLineEdit("account_system_info", self)
        self.lineEdit1.setGeometry(250, 100, 400, 30)
        # execute SQL query using execute() method.

        buttonWindow2 = QPushButton('Add publihser', self)
        buttonWindow2.setGeometry(70, 200, 150, 30)
        buttonWindow2.clicked.connect(self.buttonWindow4_onClick)
        # inputs are like this: p_id, username, password, created_day, budget, first_name, last_name, phone, address, user_type , uni_job
        self.lineEdit2 = QLineEdit("11,'Iran_Tehran_1000','www.db.com'",
                                   self)
        self.lineEdit2.setGeometry(250, 200, 400, 30)

        #
        buttonWindow3 = QPushButton('Add book', self)
        buttonWindow3.setGeometry(70, 250, 150, 30)
        buttonWindow3.clicked.connect(self.buttonWindow5_onClick)
        self.lineEdit3 = QLineEdit("11,'Math','educational',20,200,1,'ashkan'", self)
        self.lineEdit3.setGeometry(250, 250, 400, 30)

        buttonWindow4 = QPushButton('Borrow book', self)
        buttonWindow4.setGeometry(70, 300, 150, 30)
        buttonWindow4.clicked.connect(self.buttonWindow6_onClick)
        self.lineEdit4 = QLineEdit("2,1,10,1000,0", self)
        self.lineEdit4.setGeometry(250, 300, 400, 30)
        self.show()

        layoutH = QHBoxLayout()
        layoutV.addLayout(layoutH)
        layoutH.addWidget(label1)
        layoutH.addWidget(self.button)

        self.setLayout(layoutV)

    @pyqtSlot()
    def buttonWindow3_onClick(self):
        input = self.lineEdit1.text()

        # account_system_info
        cursor = db.cursor()
        q = "select * from " + str(input) + " where 1"
        print('que : ')
        print(q)
        try:
            cursor.execute(q)
            df = list(cursor.fetchall())
            # print(df)
        except pymysql.err.ProgrammingError as err:
            print(err)
            self.statusBar().showMessage(err)

        class TableModel(QtCore.QAbstractTableModel):
            def __init__(self, data):
                super(TableModel, self).__init__()
                self._data = data

            def data(self, index, role):
                if role == Qt.DisplayRole:
                    # See below for the nested-list data structure.
                    # .row() indexes into the outer list,
                    # .column() indexes into the sub-list
                    return self._data[index.row()][index.column()]

            def rowCount(self, index):
                # The length of the outer list.
                return len(self._data)

            def columnCount(self, index):
                # The following takes the first sub-list, and returns
                # the length (only works if all rows are an equal length)
                return len(self._data[0])

        class MainWindow(QtWidgets.QMainWindow):
            def __init__(self):
                super().__init__()

                self.table = QtWidgets.QTableView()
                data = []
                for item in df:
                    data_1 = []
                    for term in item:
                        data_1.append(term)
                    data.append(data_1)
                self.model = TableModel(data)
                self.table.setModel(self.model)

                self.setCentralWidget(self.table)

        self.cams = MainWindow()
        self.cams.show()
        self.close()

    @pyqtSlot()
    def buttonWindow4_onClick(self):
        input = self.lineEdit2.text()
        input = input.split(',')
        cursor = db.cursor()
        value = "(" + input[0] + ',' + input[1] + ',' + input[2] + ")"
        sql = "INSERT INTO " + "publisher(pub_id, pub_address, pub_website)" + " VALUES " + value
        try:

            cursor.execute(sql)

            db.commit()
            df = list(cursor.fetchall())
            print('Successfullyi')
            print(list(df))
        except pymysql.err.ProgrammingError as err:
            print(err)
            self.statusBar().showMessage(err)
        self.cams = Window4(self.lineEdit2.text())
        self.cams.show()
        self.close()

    @pyqtSlot()
    def buttonWindow5_onClick(self):
        input = self.lineEdit3.text()
        input = input.split(',')
        print('The input : ')
        print(input)
        cursor = db.cursor()
        value = "(" + input[0] + ',' + input[1] + ',' + input[2] + ',' + input[3] + ',' + input[4] + ',' + input[
            5] + ',' + input[6] + ")"
        sql = "INSERT INTO " + "books(b_id, b_title, b_category, b_num_of_pages, b_price, pub_id, b_author)" + " VALUES " + value
        print('sql : ')
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            df = list(cursor.fetchall())
            print('Successfullyi')
            print(list(df))
        except pymysql.err.ProgrammingError as err:
            print(err)
            self.statusBar().showMessage(err)

        self.cams = Window4(self.lineEdit3.text())
        self.cams.show()
        self.close()

    @pyqtSlot()
    def buttonWindow6_onClick(self):
        input = self.lineEdit4.text()
        input = input.split(',')
        cursor = db.cursor()
        value = "(" + input[0] + ',' + input[1] + ',' + input[2] + ',' + input[3] + ',' + input[4] + ")"
        now = datetime.now()
        print(now)
        sql = "INSERT INTO " + "borrow_history(borr_id, b_id, limit_days, borr_cost, isbacked)" + " VALUES " + value
        print('sql : ')
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            df = list(cursor.fetchall())
            print('Successfullyi')
            print(list(df))
        except pymysql.err.ProgrammingError as err:
            print(err)
            self.statusBar().showMessage(err)
        self.cams = Window4(self.lineEdit2.text())
        self.cams.show()
        self.close()

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()


class Window5(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Table Display')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))

        label1 = QLabel(value)
        self.button = QPushButton()
        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
        self.pushButton.setText('Last window')
        self.pushButton.clicked.connect(self.goMainWindow)
        layoutV.addWidget(self.pushButton)

        layoutH = QHBoxLayout()
        layoutH.addWidget(label1)
        layoutH.addWidget(self.button)
        layoutV.addLayout(layoutH)
        self.setLayout(layoutV)

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()


class Window2(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Window2')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))

        label1 = QLabel(value)
        self.button = QPushButton()
        self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.button.setIcon(self.style().standardIcon(QStyle.SP_ArrowLeft))
        self.button.setIconSize(QSize(200, 200))

        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
        self.pushButton.setText('Last window')
        self.pushButton.clicked.connect(self.goMainWindow)
        layoutV.addWidget(self.pushButton)

        layoutH = QHBoxLayout()
        layoutH.addWidget(label1)
        layoutH.addWidget(self.button)
        layoutV.addLayout(layoutH)
        self.setLayout(layoutV)

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())

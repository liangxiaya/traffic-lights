# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

# import main
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import sys
import time
from main import Basic_function
# class Ui_Dialog(object):
from PyQt5.QtWidgets import QApplication, QWidget , QVBoxLayout , QListView, QMessageBox
from PyQt5.QtCore import QStringListModel
import mainmain
class Ui_Dialog(QWidget):
    def setupUi(self, Dialog):
        # Dialog.setObjectName("pet")
        Dialog.resize(649, 522)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(330, 520, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setObjectName("buttonBox")
        self.start = QtWidgets.QPushButton(Dialog)
        self.start.setGeometry(QtCore.QRect(20, 10, 81, 41))
        self.start.setObjectName("start")
        self.Hunger_Bar = QtWidgets.QProgressBar(Dialog)
        self.Hunger_Bar.setEnabled(True)

        # self.bt2 = QPushButton('开始', self)
        # self.bt2.move(200, 50)
        # self.count = 10
        self.count = 3  #测试
        self.start.clicked.connect(self.Action)
        self.time = QTimer(self)
        self.time.setInterval(1000)
        self.time.timeout.connect(self.Refresh_hunger)
        self.mainmain = mainmain.Basic_function(50,50)


        # self.water_count = 20
        self.water_count = 5
        # self.start.clicked.connect(self.Refresh_water())
        self.water_time=QTimer(self)
        self.water_time.setInterval(1000)
        self.water_time.timeout.connect(self.Refresh_water)

        # self.show()
        self.list = []

        self.Hunger_Bar.setGeometry(QtCore.QRect(20, 140, 171, 31))
        self.Hunger_Bar.setProperty("value", 24)
        # self.Hunger_Bar.setProperty("value", str(self.mainmain.value_of_hunger))
        self.Hunger_Bar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 100, 81, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(510, 440, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.suspend = QtWidgets.QPushButton(Dialog)
        self.suspend.setGeometry(QtCore.QRect(120, 10, 81, 41))
        self.suspend.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 110, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.water_Bar = QtWidgets.QProgressBar(Dialog)
        self.water_Bar.setEnabled(True)
        self.water_Bar.setGeometry(QtCore.QRect(310, 140, 171, 31))
        self.water_Bar.setProperty("value", 24)
        self.water_Bar.setObjectName("progressBar_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(310, 100, 81, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(470, 110, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        ##日志
        self.journal = QtWidgets.QTextBrowser(Dialog)
        # self.modil= QStringListModel()
        # self.modil.setStringList(self.list)
        # self.journal.setModel(self.modil)
        self.journal.setGeometry(QtCore.QRect(20, 230, 256, 192))
        self.journal.setObjectName("listView")
        # self.journal.setStringList(self.list)


        ##需要输出的集合
        self.info = [self.mainmain.value_of_hunger,self.mainmain.value_of_water]


        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 210, 54, 12))
        self.label_3.setObjectName("label_3")
        self.input_value_of_hunger = QtWidgets.QTextEdit(Dialog)
        # self.input_value_of_hunger.QLineEdit(self)
        self.input_value_of_hunger.setGeometry(QtCore.QRect(410, 240, 101, 31))
        self.input_value_of_hunger.setObjectName("textEdit")
        self.Data_submission = QtWidgets.QPushButton(Dialog)
        self.Data_submission.setGeometry(QtCore.QRect(540, 250, 51, 41))
        self.Data_submission.setObjectName("pushButton_5")
        self.input_value_of_water = QtWidgets.QTextEdit(Dialog)
        self.input_value_of_water.setGeometry(QtCore.QRect(410, 280, 101, 31))
        self.input_value_of_water.setObjectName("textEdit_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(320, 220, 81, 41))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.pushButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.suspend.clicked.connect(self.Action_stop)    ##暂停事件
        self.Data_submission.clicked.connect(self.Action_submission)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "pet"))
        self.start.setText(_translate("Dialog", "start"))
        self.label.setText(_translate("Dialog", "饥饿值："))
        self.pushButton.setText(_translate("Dialog", "关闭窗口"))
        self.suspend.setText(_translate("Dialog", "暂停"))
        self.pushButton_3.setText(_translate("Dialog", "倒计时"))
        self.label_2.setText(_translate("Dialog", "口渴值："))
        self.pushButton_4.setText(_translate("Dialog", "倒计时"))
        # 第二次添加  还有两个提交的参数
        self.label_3.setText(_translate("Dialog", "日志"))
        self.Data_submission.setText(_translate("Dialog", "提交"))
        self.label_4.setText(_translate("Dialog", "属性值更改："))


    def Action(self):
        if self.start.isEnabled():
            self.time.start()
            self.water_time.start()
            # self.start.setEnabled(False)
    def Action_stop(self):
        # if self.start.isEnabled():
        self.time.stop()
        self.water_time.stop()
    def Action_uncount(self):
        self.count
    # def Action_submission(self):
    # def
    def Action_submission(self):
        self.mainmain.value_of_hunger=int(self.input_value_of_hunger.toPlainText())
        self.mainmain.value_of_water=int(self.input_value_of_water.toPlainText())
        self.info = [self.mainmain.value_of_hunger,self.mainmain.value_of_water]
        print(self.info)
        return self.info
    def Refresh_water(self):
        self.Hunger_Bar.setProperty("value", str(self.mainmain.value_of_hunger))
        self.water_Bar.setProperty("value", str(self.mainmain.value_of_water))

        if self.water_count > 0:
            # self.start.setText(str(self.count) + '秒')
            self.water_Bar.setProperty("value", str(self.mainmain.value_of_water))
            if self.mainmain.value_of_water < 45:  # 简易阈值
                print("WARING")
                self.list.append("WARING")
            # main.Basic_function.changed_hunger(main.Basic_function.value_of_hunger)
            # self.pushButton_3.setText("倒计时：",self.count)
            self.label_2.setText("口渴值：" + str(self.mainmain.value_of_water))
            print("water倒计时中" + str(self.water_count) + '秒')

            self.water_count -= 1
            self.pushButton_4.setText("倒计时：" + str(self.water_count))

            # if self.count == 0:
            #     self.changed_water()
        else:
            # self.Action_stop()
            self.water_time.stop()
            self.list.append(self.info)
            self.info = ["饥饿值:" + str(self.mainmain.value_of_hunger), "口渴值" + str(self.mainmain.value_of_water)]


            self.label.setText("饥饿值：" + str(self.mainmain.value_of_hunger))
            print("water倒计时中" + str(self.water_count) + '秒')
            # print("饥饿值：" + str(self.mainmain.value_of_hunger))
            # print("口渴值：" + str(self.mainmain.value_of_water))



            self.journal.setText(str(self.list))  # 可实现
            self.pushButton_4.setText("倒计时：" + str(self.water_count))
            self.mainmain.changed_water(self.mainmain.value_of_water)
            self.label_2.setText("口渴值：" + str(self.mainmain.value_of_water))
            # self.changed_water()
            # self.start.setEnabled(True)
            self.start.setText('开始')
            self.water_Bar.setProperty("value", str(self.mainmain.value_of_water))
            # self.count = 10
            self.water_count = 5  # 测试
            self.water_time.start()



    def Refresh_hunger(self):
        self.Hunger_Bar.setProperty("value", str(self.mainmain.value_of_hunger))
        self.water_Bar.setProperty("value", str(self.mainmain.value_of_water))
        # self.journal.setText("倒计时中"+str(self.count)+'秒',"饥饿值："+str(self.mainmain.value_of_hunger),"口渴值："+str(self.mainmain.value_of_water))
        # self.journal.setText("倒计时中"+str(self.count)+'秒')   #可实现
        # print(list)


        # if self.water_count > 0:
        #     self.info = ["饥饿值:" + str(self.mainmain.value_of_hunger), "口渴值" + str(self.mainmain.value_of_water)]
        #     # self.info = ["饥饿值："+self.mainmain.value_of_hunger,"口渴值："+self.mainmain.value_of_water]
        #     self.list.append(self.info)
        #     self.journal.setText(str(self.list))  # 可实现
        #     self.start.setText(str(self.count) + '秒')
        #     if self.mainmain.value_of_water < 45:  # 简易阈值
        #         print("WARING")
        #         self.list.append("WARING")
        #     # main.Basic_function.changed_hunger(main.Basic_function.value_of_hunger)
        #     # self.pushButton_3.setText("倒计时：",self.count)
        #     self.pushButton_3.setText("倒计时：" + str(self.count))
        #     self.label.setText("饥饿值：" + str(self.mainmain.value_of_hunger))
        #     print("倒计时中" + str(self.count) + '秒')
        #     print("饥饿值：" + str(self.mainmain.value_of_hunger))
        #     print("口渴值：" + str(self.mainmain.value_of_water))
        #     self.water_count -= 1
        #     # if self.count == 0:
        #     #     self.changed_water()
        # else:
        #     self.time.stop()
        #     self.pushButton_3.setText("倒计时：" + str(self.count))
        #     self.mainmain.changed_hunger(self.mainmain.value_of_hunger)
        #     self.label.setText("饥饿值：" + str(self.mainmain.value_of_hunger))
        #     # self.changed_water()
        #     # self.start.setEnabled(True)
        #     self.start.setText('开始')
        #     self.Hunger_Bar.setProperty("value", str(self.mainmain.value_of_hunger))
        #     # self.count = 10
        #     self.water_count = 5  # 测试
        #
        #
        # if self.count > 0:
        #     self.info = ["饥饿值:"+str(self.mainmain.value_of_hunger),"口渴值"+str(self.mainmain.value_of_water)]
        #     # self.info = ["饥饿值："+self.mainmain.value_of_hunger,"口渴值："+self.mainmain.value_of_water]
        #     self.list.append(self.info)
        #     self.journal.setText(str(self.list))  # 可实现
        #     self.start.setText(str(self.count) +'秒')
        #     if self.mainmain.value_of_hunger < 45:   #简易阈值
        #         print("WARING")
        #         self.list.append("WARING")
        #     # main.Basic_function.changed_hunger(main.Basic_function.value_of_hunger)
        #     # self.pushButton_3.setText("倒计时：",self.count)
        #     self.pushButton_3.setText("倒计时："+str(self.count))
        #     self.label.setText("饥饿值："+str(self.mainmain.value_of_hunger))
        #     print("倒计时中"+str(self.count)+'秒')
        #     print("饥饿值："+str(self.mainmain.value_of_hunger))
        #     print("口渴值："+str(self.mainmain.value_of_water))
        #     self.count -= 1
        # # if self.count == 0:
        # #     self.changed_water()
        # else:
        #     self.time.stop()
        #     self.pushButton_3.setText("倒计时："+str(self.count))
        #     self.mainmain.changed_hunger(self.mainmain.value_of_hunger)
        #     self.label.setText("饥饿值："+str(self.mainmain.value_of_hunger))
        #     # self.changed_water()
        #     # self.start.setEnabled(True)
        #     self.start.setText('开始')
        #     self.Hunger_Bar.setProperty("value", str(self.mainmain.value_of_hunger))
        #     # self.count = 10
        #     self.count = 3   #测试
        #------------------__________=--------------    解决双时钟冲突问题





        if self.count > 0:
            self.info = ["饥饿值:"+str(self.mainmain.value_of_hunger),"口渴值"+str(self.mainmain.value_of_water)]
            self.list.append(self.info)
            self.journal.setText(str(self.list))  # 可实现
            self.start.setText(str(self.count) +'秒')
            if self.mainmain.value_of_hunger < 45:   #简易阈值
                print("WARING")
                self.list.append("WARING")
            self.pushButton_3.setText("倒计时："+str(self.count))
            self.label.setText("饥饿值："+str(self.mainmain.value_of_hunger))
            print("hunger倒计时中"+str(self.count)+'秒')
            self.count -= 1
        else:
            self.time.stop()
            self.pushButton_3.setText("倒计时："+str(self.count))
            self.mainmain.changed_hunger(self.mainmain.value_of_hunger)
            self.label.setText("饥饿值："+str(self.mainmain.value_of_hunger))
            # self.changed_water()
            # self.start.setEnabled(True)
            self.start.setText('开始')
            self.Hunger_Bar.setProperty("value", str(self.mainmain.value_of_hunger))
            # self.count = 10
            self.count = 3   #测试
            self.time.start()

    def Count_time(self):

# import sys
import time
# import datetime
# import os
# from PyQt5.QtCore import QObject , pyqtSignal
# import msvcrt
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
# from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import QMainWindow, QPushButton , QWidget , QMessageBox, QApplication, QHBoxLayout,QDialog
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer


import untitled
#--------------------------------------------------------------------
class Basic_function:
    def __init__(self,redlight_count, greanlight_count):
        # 初始化属性设置
        self.redlight_count = redlight_count
        self.greanlight_count = greanlight_count

    def get_descriptive_info(self):
        # 返回属性值
        #     info = f'饥饿值：{self.value_of_hunger}\n水份：{self.value_of_water}'

        info = [self.redlight_count,self.greanlight_count]
        print(info)

        # print("饥饿值: ", info['self.value_h'])
        # print("口渴值: ", info['self.value_w'])
        # time.sleep(3)
        return info


    # def changed_lights(self, redlight_count):
    #     #将读数递减
    #         time.sleep(1)
    #         self.redlight_count = self.redlight_count-reduce_lights
    #         print(redlight_count)
    #         return self.redlight_count
    #------------------------------------------  可以优化自减
    def changed_lights(self, redlight_count):
        #将读数递减
            time.sleep(1)
            self.redlight_count = self.redlight_count-1
            print(redlight_count)
            return self.redlight_count
    # if self.value_of_hunger == 0:
    #
    # def changed_water(self, value_of_water):
    #         time.sleep(1)
    #         self.value_of_water =self.value_of_water-reduce_water
    #         if a.value_of_water < 0:
    #             a.value_of_water = 0
    #             # print(a.value_of_water)
    #             sys.exit(0)
    #             # break
    #         return self.value_of_water

            # if self.value_of_water == 0:
    def local_time(self):
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
        now2 = time.strftime("%Y-%m-%d", time.localtime())
        print(now)
        print(now2)
        #获取系统时间
#————————————————————————————————————————————————————————————————————————————
# class Ui_Dialog(object):
#     def setupUi(self, Dialog):
#         Dialog.setObjectName("Dialog")
#         Dialog.resize(649, 522)
#         self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
#         self.buttonBox.setGeometry(QtCore.QRect(330, 520, 341, 32))
#         self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
#         self.buttonBox.setObjectName("buttonBox")
#         self.start = QtWidgets.QPushButton(Dialog)
#         self.start.setGeometry(QtCore.QRect(20, 10, 81, 41))
#         self.start.setObjectName("start")
#         self.progressBar = QtWidgets.QProgressBar(Dialog)
#         self.progressBar.setEnabled(True)
#         self.progressBar.setGeometry(QtCore.QRect(20, 140, 171, 31))
#         self.progressBar.setProperty("value", a.value_of_hunger)
#         self.progressBar.setObjectName("progressBar")
#         self.label = QtWidgets.QLabel(Dialog)
#         self.label.setGeometry(QtCore.QRect(20, 100, 61, 31))
#         self.label.setObjectName("label")
#         self.pushButton = QtWidgets.QPushButton(Dialog)
#         self.pushButton.setGeometry(QtCore.QRect(510, 440, 75, 23))
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton_2 = QtWidgets.QPushButton(Dialog)
#         self.pushButton_2.setGeometry(QtCore.QRect(120, 10, 81, 41))
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.pushButton_3 = QtWidgets.QPushButton(Dialog)
#         self.pushButton_3.setGeometry(QtCore.QRect(190, 110, 75, 23))
#         self.pushButton_3.setObjectName("pushButton_3")
#         self.progressBar_2 = QtWidgets.QProgressBar(Dialog)
#         self.progressBar_2.setEnabled(True)
#         self.progressBar_2.setGeometry(QtCore.QRect(310, 140, 171, 31))
#         self.progressBar_2.setProperty("value", a.value_of_water)
#         self.progressBar_2.setObjectName("progressBar_2")
#         self.label_2 = QtWidgets.QLabel(Dialog)
#         self.label_2.setGeometry(QtCore.QRect(310, 100, 61, 31))
#         self.label_2.setObjectName("label_2")
#         self.pushButton_4 = QtWidgets.QPushButton(Dialog)
#         self.pushButton_4.setGeometry(QtCore.QRect(470, 110, 75, 23))
#         self.pushButton_4.setObjectName("pushButton_4")
#         self.retranslateUi(Dialog)
#         self.buttonBox.accepted.connect(Dialog.accept)
#         self.buttonBox.rejected.connect(Dialog.reject)
#         self.pushButton.clicked.connect(Dialog.close)
#         QtCore.QMetaObject.connectSlotsByName(Dialog)
#
#     def retranslateUi(self, Dialog):
#         _translate = QtCore.QCoreApplication.translate
#         Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
#         # self.bt2.setText(_translate("Dialog", "start"))
#         self.label.setText(_translate("Dialog", "饥饿值："))
#         self.pushButton.setText(_translate("Dialog", "关闭窗口"))
#         self.pushButton_2.setText(_translate("Dialog", "暂停"))
#         self.pushButton_3.setText(_translate("Dialog", "倒计时"))
#         self.label_2.setText(_translate("Dialog", "口渴值："))
#         self.pushButton_4.setText(_translate("Dialog", "倒计时"))

    # def initUI(self):
    #         self.resize(400, 300)
    #         self.setWindowTitle('pet')  ##标题
    #         bt1 = QPushButton("这是什么", self)
    #         bt1.move(50, 50)
    #         self.bt2 = QPushButton('开始', self)
    #         self.bt2.move(200, 50)
    #         self.count = 10
    #         self.bt2.clicked.connect(self.Action)
    #         self.time = QTimer(self)
    #         self.time.setInterval(1000)
    #         self.time.timeout.connect(self.Refresh)
    #
    #         self.show()
    #         """
    # 我们单击按钮后，进行判断若按钮没有被禁用，则激活定时器，同时将按钮禁用，即禁止点击。
    #         """
    #
    # def Action(self):
    #     if self.bt2.isEnabled():
    #         self.time.start()
    #         self.bt2.setEnabled(False)
    #     """
    # 进入超时状态后，我们开始倒计时。同时让按钮上的文字不断的在变化。
    # 当倒计时完成的时候，我们停止定时器。将按钮恢复成正常的状态。同时重置倒计时的值，为下次的使用做好准备。
    #         """
    #
    # def Refresh(self):
    #     if self.count > 0:
    #         self.bt2.setText(str(self.count) + '秒')
    #         # print(info)
    #         print(str(self.count) + '秒')
    #         Basic_function.changed_hunger()
    #         # print(Basic_function.value_of_hunger)
    #         self.count -= 1
    #     # if self.count == 0:
    #     #     self.changed_water()
    #     else:
    #         self.time.stop()
    #         self.changed_water()
    #         self.bt2.setEnabled(True)
    #         self.bt2.setText('开始')
    #         self.count = 10


#————————————————————————————————————————————————————————————————————————————

water = 100
hunger = 100
reduce_lights = 1
a = Basic_function(water, hunger)
print("**********start**********")
a.local_time()
var = 1
redlight_count=0
greanlight_count=0

if a.redlight_count == 0:
    print("红灯结束")

# while var ==1:
# a.get_descriptive_info()
# time.sleep(3)                                            调试关闭
# if a.value_of_water < 30:
#     print("**我有点渴了**")
#     # time.sleep(1)
# if a.value_of_hunger < 30:
#     print("**我有点饿了**")
#     # time.sleep(1)
# if a.value_of_hunger < 0:
#     a.value_of_hunger=0
#     print(a.value_of_hunger)
#     print("由于饥饿而死")
#     # sys.exit(0)
#     # break
    # if a.value_of_water < 0:
    #     a.value_of_water=0
    #     print(a.value_of_water)
    #     print("由于口渴而死")
    #     # sys.exit(0)
    #     break
    # print(a.get_descriptive_info().info)

# if a.value_of_water < 30:
#      print("**我有点渴了**")
#      time.sleep(1)
# if a.value_of_hunger <30:
#     print("**我有点饿了**")
#     time.sleep(1)
# if a.value_of_hunger <0:
#     print("由于饥饿而死")
# if a.value_of_water <0:
#     print("由于口渴而死")

#---------------------------------------------------------测试绑定函数
if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    MainWindow = QDialog()
    ui=untitled.Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())












#------------------------------------------------------------------

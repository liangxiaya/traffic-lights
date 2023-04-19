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
import untitled_new



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

    #




    #     """
    # # 进入超时状态后，我们开始倒计时。同时让按钮上的文字不断的在变化。
    # # 当倒计时完成的时候，我们停止定时器。将按钮恢复成正常的状态。同时重置倒计时的值，为下次的使用做好准备。
    # #         """
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

# class Ui_Dialog(object):
#     def setupUi(self, Dialog):
#         Dialog.setObjectName("Dialog")
#         Dialog.resize(618, 479)
#         self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
#         self.buttonBox.setGeometry(QtCore.QRect(330, 520, 341, 32))
#         self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
#         self.buttonBox.setObjectName("buttonBox")
#         self.start_box = QtWidgets.QPushButton(Dialog)
#         self.start_box.setGeometry(QtCore.QRect(20, 10, 81, 41))
#         self.start_box.setObjectName("start_box")
#         self.left_light_label = QtWidgets.QLabel(Dialog)
#         self.left_light_label.setGeometry(QtCore.QRect(20, 80, 91, 31))
#         self.left_light_label.setObjectName("left_light_label")
#         self.pushButton = QtWidgets.QPushButton(Dialog)
#         self.pushButton.setGeometry(QtCore.QRect(510, 440, 75, 23))
#         self.pushButton.setObjectName("pushButton")
#         self.zanting_box = QtWidgets.QPushButton(Dialog)
#         self.zanting_box.setGeometry(QtCore.QRect(120, 10, 81, 41))
#         self.zanting_box.setObjectName("zanting_box")
#         self.mid_light_label = QtWidgets.QLabel(Dialog)
#         self.mid_light_label.setGeometry(QtCore.QRect(240, 80, 61, 31))
#         self.mid_light_label.setObjectName("mid_light_label")
#         self.left_lightbox = QtWidgets.QPushButton(Dialog)
#         self.left_lightbox.setGeometry(QtCore.QRect(60, 120, 100, 100))
#         self.left_lightbox.setMaximumSize(QtCore.QSize(100, 100))
#         self.left_lightbox.setAccessibleDescription("")
#         self.left_lightbox.setStyleSheet("QPushButton{\n"
# "background-color:rgb(255,0,0);\n"
# "color:white;\n"
# "brorder-radius:50px;\n"
# "border:2px groove gray;\n"
# "border-style:outset;\n"
# "}")
#         self.left_lightbox.setObjectName("left_lightbox")
#         self.comboBox = QtWidgets.QComboBox(Dialog)
#         self.comboBox.setGeometry(QtCore.QRect(160, 90, 69, 22))
#         self.comboBox.setObjectName("comboBox")
#         self.comboBox.addItem("")
#         self.comboBox.addItem("")
#         self.comboBox_2 = QtWidgets.QComboBox(Dialog)
#         self.comboBox_2.setGeometry(QtCore.QRect(340, 90, 69, 22))
#         self.comboBox_2.setObjectName("comboBox_2")
#         self.comboBox_2.addItem("")
#         self.comboBox_2.addItem("")
#         self.mid_lightbox = QtWidgets.QPushButton(Dialog)
#         self.mid_lightbox.setGeometry(QtCore.QRect(230, 120, 100, 100))
#         self.mid_lightbox.setMaximumSize(QtCore.QSize(100, 100))
#         self.mid_lightbox.setAccessibleDescription("")
#         self.mid_lightbox.setStyleSheet("QPushButton{\n"
# "background-color:rgb(255,0,0);\n"
# "color:white;\n"
# "brorder-radius:50px;\n"
# "border:2px groove gray;\n"
# "border-style:outset;\n"
# "}")
#         self.mid_lightbox.setObjectName("mid_lightbox")
#         self.right_lightbox = QtWidgets.QPushButton(Dialog)
#         self.right_lightbox.setGeometry(QtCore.QRect(400, 120, 100, 100))
#         self.right_lightbox.setMaximumSize(QtCore.QSize(100, 100))
#         self.right_lightbox.setAccessibleDescription("")
#         self.right_lightbox.setStyleSheet("QPushButton{\n"
# "background-color:rgb(255,0,0);\n"
# "color:white;\n"
# "brorder-radius:50px;\n"
# "border:2px groove gray;\n"
# "border-style:outset;\n"
# "}")
#         self.right_lightbox.setObjectName("right_lightbox")
#         self.comboBox_3 = QtWidgets.QComboBox(Dialog)
#         self.comboBox_3.setGeometry(QtCore.QRect(500, 90, 69, 22))
#         self.comboBox_3.setObjectName("comboBox_3")
#         self.comboBox_3.addItem("")
#         self.comboBox_3.addItem("")
#         self.comboBox_4 = QtWidgets.QComboBox(Dialog)
#         self.comboBox_4.setGeometry(QtCore.QRect(160, 60, 69, 22))
#         self.comboBox_4.setObjectName("comboBox_4")
#         self.comboBox_4.addItem("")
#         self.comboBox_4.addItem("")
#         self.comboBox_4.addItem("")
#         self.comboBox_4.setItemText(2, "")
#         self.comboBox_5 = QtWidgets.QComboBox(Dialog)
#         self.comboBox_5.setGeometry(QtCore.QRect(340, 60, 69, 22))
#         self.comboBox_5.setObjectName("comboBox_5")
#         self.comboBox_5.addItem("")
#         self.comboBox_6 = QtWidgets.QComboBox(Dialog)
#         self.comboBox_6.setGeometry(QtCore.QRect(500, 60, 69, 22))
#         self.comboBox_6.setObjectName("comboBox_6")
#         self.comboBox_6.addItem("")
#         self.comboBox_6.addItem("")
#         self.comboBox_6.addItem("")
#         self.right_light_label = QtWidgets.QLabel(Dialog)
#         self.right_light_label.setGeometry(QtCore.QRect(420, 80, 61, 31))
#         self.right_light_label.setObjectName("right_light_label")
#
#         self.retranslateUi(Dialog)
#         self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
#         self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
#         self.pushButton.clicked.connect(Dialog.close) # type: ignore
#         QtCore.QMetaObject.connectSlotsByName(Dialog)
#
#     def retranslateUi(self, Dialog):
#         _translate = QtCore.QCoreApplication.translate
#         Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
#         self.start_box.setText(_translate("Dialog", "start"))
#         self.left_light_label.setText(_translate("Dialog", "灯运行了："))
#         self.pushButton.setText(_translate("Dialog", "关闭窗口"))
#         self.zanting_box.setText(_translate("Dialog", "暂停"))
#         self.mid_light_label.setText(_translate("Dialog", "灯运行了："))
#         self.left_lightbox.setText(_translate("Dialog", "灯还有0秒"))
#         self.comboBox.addItems("绿","红")
#         self.comboBox.currentIndexChanged.connect(self.left_red)
#         # self.comboBox.setItemText(0, _translate("Dialog", "绿灯"))
#         # self.comboBox.setItemText(1, _translate("Dialog", "红灯"))
#         self.comboBox_2.setItemText(0, _translate("Dialog", "绿灯"))
#         self.comboBox_2.setItemText(1, _translate("Dialog", "红灯"))
#         self.mid_lightbox.setText(_translate("Dialog", "灯还有0秒"))
#         self.right_lightbox.setText(_translate("Dialog", "灯还有0秒"))
#         self.comboBox_3.setItemText(0, _translate("Dialog", "绿灯"))
#         self.comboBox_3.setItemText(1, _translate("Dialog", "红灯"))
#         self.comboBox_4.setItemText(0, _translate("Dialog", "空"))
#         self.comboBox_4.setItemText(1, _translate("Dialog", "左转"))
#         self.comboBox_5.setItemText(0, _translate("Dialog", "直行"))
#         self.comboBox_6.setItemText(0, _translate("Dialog", "空"))
#         self.comboBox_6.setItemText(1, _translate("Dialog", "直行"))
#         self.comboBox_6.setItemText(2, _translate("Dialog", "右转"))
#         self.right_light_label.setText(_translate("Dialog", "灯运行了："))

#————————————————————————————————————————————————————————————————————————————

reduce_lights = 1
red_time =100
grean_time =100
# a = Basic_function(1,20)
print("**********start**********")
# a.local_time()
var = 1

# if a.redlight_count == 0:
#     print("红灯结束")

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

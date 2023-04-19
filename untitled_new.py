from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import sys
import time
# class Ui_Dialog(object):
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget , QVBoxLayout , QListView, QMessageBox
from PyQt5.QtCore import QStringListModel
import mainmain
from basic_model import Basic_function
import copy
class Ui_Dialog(QWidget):
    # def other_lights(self):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(618, 479)
        first_lights=[5, 6, 7,8,9,10]
        second_lights=[15, 16, 17,18,19,20]
        # (self, left_light_count, midlight_count, rightlight_count):
        #               左红  中红  右红   左绿  中绿  右绿
        # self.data_model = Basic_function(5, 6, 7,8,9,10);
        self.data_model = Basic_function(5, 6, 7,8,9,10);
        self.data_model_copy = copy.copy(self.data_model)


        # self.data_model_copy.mid_light_count = self.data_model_copy.mid_light_count
        # self.data_model_copy.mid_Green_light_count = self.data_model_copy.mid_Green_light_count
        # self.data_model_copy.right_light_count_new = self.data_model_copy.right_light_count_new
        # self.left_light_count_new = self.left_light_count_new
        # self.data_model_copy.mid_light_count_new = self.data_model_copy.mid_light_count_new




        print(self.data_model_copy.left_light_count, self.data_model_copy.mid_light_count, self.data_model_copy.right_light_count)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(330, 520, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setObjectName("buttonBox")
        self.start_box = QtWidgets.QPushButton(Dialog)
        self.start_box.setGeometry(QtCore.QRect(20, 10, 81, 41))
        self.start_box.setObjectName("start_box")


        self.left_light_label = QtWidgets.QLabel(Dialog)
        self.left_light_label.setGeometry(QtCore.QRect(20, 80, 91, 31))
        self.left_light_label.setObjectName("left_light_label")

        self.left_label_text = QtWidgets.QLabel(Dialog)
        self.left_label_text.setGeometry(QtCore.QRect(40, 260, 31, 31))
        self.left_label_text.setObjectName("left_label_text")

        self.mid_label_text = QtWidgets.QLabel(Dialog)
        self.mid_label_text.setGeometry(QtCore.QRect(40, 300, 31, 31))
        self.mid_label_text.setObjectName("mid_label_text")

        self.right_label_text = QtWidgets.QLabel(Dialog)
        self.right_label_text.setGeometry(QtCore.QRect(40, 340, 31, 31))
        self.right_label_text.setObjectName("right_label_text")






        self.red_label_text = QtWidgets.QLabel(Dialog)
        self.red_label_text.setGeometry(QtCore.QRect(120, 220, 31, 31))
        self.red_label_text.setObjectName("red_label_text")

        self.green_label_text = QtWidgets.QLabel(Dialog)
        self.green_label_text.setGeometry(QtCore.QRect(250, 220, 31, 31))
        self.green_label_text.setObjectName("green_label_text")





        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(510, 440, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.zanting_box = QtWidgets.QPushButton(Dialog)
        self.zanting_box.setGeometry(QtCore.QRect(120, 10, 81, 41))
        self.zanting_box.setObjectName("zanting_box")
        self.mid_light_label = QtWidgets.QLabel(Dialog)
        self.mid_light_label.setGeometry(QtCore.QRect(240, 80, 61, 31))
        self.mid_light_label.setObjectName("mid_light_label")
        self.left_lightbox = QtWidgets.QPushButton(Dialog)
        self.left_lightbox.setGeometry(QtCore.QRect(60, 120, 100, 100))
        self.left_lightbox.setMaximumSize(QtCore.QSize(100, 100))
        self.left_lightbox.setAccessibleDescription("")
        self.left_lightbox.setStyleSheet("QPushButton{\n"
                                         "background-color:rgb(255,0,0);\n"
                                         "color:white;\n"
                                         "brorder-radius:50px;\n"
                                         "border:2px groove gray;\n"
                                         "border-style:outset;\n"
                                         "}")
        self.start_box.clicked.connect(self.Action)
        # self.reduce_time = 1
        self.reduce_time = QTimer(self)
        self.reduce_time.setInterval(1000)
        self.reduce_time.timeout.connect(self.Refresh_light_time)
        # self.reduce_time.timeout.connect(self.Refresh_mid_light_time)
        # self.reduce_time.timeout.connect(self.Refresh_right_light_time)

        self.left_lightbox.setObjectName("left_lightbox")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(160, 90, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(340, 90, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.mid_lightbox = QtWidgets.QPushButton(Dialog)
        self.mid_lightbox.setGeometry(QtCore.QRect(230, 120, 100, 100))
        self.mid_lightbox.setMaximumSize(QtCore.QSize(100, 100))
        self.mid_lightbox.setAccessibleDescription("")
        self.mid_lightbox.setStyleSheet("QPushButton{\n"
                                        "background-color:rgb(255,0,0);\n"
                                        "color:white;\n"
                                        "brorder-radius:50px;\n"
                                        "border:2px groove gray;\n"
                                        "border-style:outset;\n"
                                        "}")
        self.mid_lightbox.setObjectName("mid_lightbox")
        self.right_lightbox = QtWidgets.QPushButton(Dialog)
        self.right_lightbox.setGeometry(QtCore.QRect(400, 120, 100, 100))
        self.right_lightbox.setMaximumSize(QtCore.QSize(100, 100))
        self.right_lightbox.setAccessibleDescription("")
        self.right_lightbox.setStyleSheet("QPushButton{\n"
                                          "background-color:rgb(255,0,0);\n"
                                          "color:white;\n"
                                          "brorder-radius:50px;\n"
                                          "border:2px groove gray;\n"
                                          "border-style:outset;\n"
                                          "}")
        self.right_lightbox.setObjectName("right_lightbox")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(500, 90, 69, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(160, 60, 69, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setItemText(2, "")
        self.comboBox_5 = QtWidgets.QComboBox(Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(340, 60, 69, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_6 = QtWidgets.QComboBox(Dialog)
        self.comboBox_6.setGeometry(QtCore.QRect(500, 60, 69, 22))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.right_light_label = QtWidgets.QLabel(Dialog)
        self.right_light_label.setGeometry(QtCore.QRect(420, 80, 61, 31))
        self.right_light_label.setObjectName("right_light_label")
        self.shuxing = QtWidgets.QLabel(Dialog)
        self.shuxing.setGeometry(QtCore.QRect(340, 250, 81, 41))
        self.shuxing.setObjectName("shuxing")

        self.change_left = QtWidgets.QTextEdit(Dialog)
        self.change_left.setGeometry(QtCore.QRect(90, 260, 101, 31))
        self.change_left.setObjectName("change_left")
        self.change_mid = QtWidgets.QTextEdit(Dialog)
        self.change_mid.setGeometry(QtCore.QRect(90, 300, 101, 31))
        self.change_mid.setObjectName("change_mid")
        self.change_right = QtWidgets.QTextEdit(Dialog)
        self.change_right.setGeometry(QtCore.QRect(90, 340, 101, 31))
        self.change_right.setObjectName("change_right")

        self.change_left_red = QtWidgets.QTextEdit(Dialog)
        self.change_left_red.setGeometry(QtCore.QRect(210, 260, 101, 31))
        self.change_left_red.setObjectName("change_left_red")
        self.change_mid_red = QtWidgets.QTextEdit(Dialog)
        self.change_mid_red.setGeometry(QtCore.QRect(210, 300, 101, 31))
        self.change_mid_red.setObjectName("change_mid_red")
        self.change_right_red = QtWidgets.QTextEdit(Dialog)
        self.change_right_red.setGeometry(QtCore.QRect(210, 340, 101, 31))
        self.change_right_red.setObjectName("change_right_red")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(340, 280, 51, 41))
        self.pushButton_5.setObjectName("pushButton_5")

        self.light_switch = QtWidgets.QComboBox(Dialog)
        self.light_switch.setGeometry(QtCore.QRect(250, 10, 101, 41))
        self.light_switch.setObjectName("light_switch")
        self.light_switch.addItem("diyi")
        self.light_switch.addItem("dier")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)  # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject)  # type: ignore
        self.pushButton.clicked.connect(Dialog.close)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_5.clicked.connect(self.Action_submission)
        self.zanting_box.clicked.connect(self.Action_stop)
        # self.light_switch.currentIndexChanged.connect(self.Action_witch_light())
        self.light_switch.currentIndexChanged.connect(self.Action_witch_light)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.start_box.setText(_translate("Dialog", "start"))
        self.left_light_label.setText(_translate("Dialog", "灯运行了："))
        self.left_label_text.setText(_translate("Dialog", "左灯"))
        self.mid_label_text.setText(_translate("Dialog", "中灯"))
        self.right_label_text.setText(_translate("Dialog", "右灯"))
        self.green_label_text.setText(_translate("Dialog", "红灯"))
        self.red_label_text.setText(_translate("Dialog", "绿灯"))
        self.pushButton.setText(_translate("Dialog", "关闭窗口"))
        self.zanting_box.setText(_translate("Dialog", "暂停"))
        self.mid_light_label.setText(_translate("Dialog", "灯运行了："))
        self.left_lightbox.setText(_translate("Dialog", "灯还有0秒"))
        self.comboBox.setItemText(0, _translate("Dialog", "绿灯"))
        self.comboBox.setItemText(1, _translate("Dialog", "红灯"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "绿灯"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "红灯"))
        self.mid_lightbox.setText(_translate("Dialog", "灯还有0秒"))
        self.right_lightbox.setText(_translate("Dialog", "灯还有0秒"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "绿灯"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "红灯"))
        self.comboBox_4.setItemText(0, _translate("Dialog", "空"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "左转"))
        self.comboBox_5.setItemText(0, _translate("Dialog", "直行"))
        self.comboBox_6.setItemText(0, _translate("Dialog", "空"))
        self.comboBox_6.setItemText(1, _translate("Dialog", "直行"))
        self.comboBox_6.setItemText(2, _translate("Dialog", "右转"))
        self.right_light_label.setText(_translate("Dialog", "灯运行了："))
        self.pushButton_5.setText(_translate("Dialog", "提交"))
        self.light_switch.setItemText(0, _translate("Dialog", "第一个红绿灯"))
        self.light_switch.setItemText(1, _translate("Dialog", "第二个红绿灯"))
        # self.label_4.setText(_translate("Dialog", "属性值更改："))
    def Action(self):
        if self.start_box.isEnabled():
            self.reduce_time.start()
            # self.data_model_copy = self.data_model



    def Action_witch_light(self,i):
        # print("xuanze")
        for count in range(self.light_switch.count()):
            print('item' + str(count) + '=' + self.light_switch.itemText(count))
            print("Current index", i, "selection changed ", self.light_switch.currentText())





    def Action_stop(self):
        print("time stop")
        self.reduce_time.stop()
    def reduce_time(self):
        totalTime = 5
        if totalTime.isdigit():
            print(totalTime)
            totalTime = int(totalTime)
            while totalTime > 0:
                print('还剩%d秒' % totalTime)
                time.sleep(1)
                totalTime -= 1
            print("时间到")
        else:
            print("请输入整数")
        return 0









    #   2. 三框倒计时
    def Refresh_light_time(self):
        self.Refresh_left_light_time()
        self.Refresh_mid_light_time()
        self.Refresh_right_light_time()
        self.lights_count = 1
        self.lights_count += 1

    def Refresh_left_light_time(self):
        if self.data_model_copy.left_light_count >= 0:
            # print("self.data_model_copy.mid_light_count", self.data_model_copy.mid_light_count)
            self.left_lightbox.setStyleSheet("color:white;\n""background-color:rgb(255,0,0)")
            self.left_light_label.setText("运行了：" + str(self.data_model_copy.left_light_count))
            self.left_lightbox.setText("左灯还有：" + str(self.data_model_copy.left_light_count))
            if self.data_model_copy.left_light_count <= 3:
                if self.data_model_copy.left_light_count % 2 == 0:
                    self.left_light_twinkle()
                else:
                    self.left_light_twinkle_two()
            self.data_model_copy.left_light_count -= 1
        else:
            if self.data_model_copy.left_Green_light_count > 0:
                self.left_lightbox.setStyleSheet("color:white;\n""background-color:rgb(0,255,0)")
                self.left_light_label.setText("左灯运行：" + str(self.data_model_copy.left_Green_light_count))
                self.left_lightbox.setText("左灯还有：" + str(self.data_model_copy.left_Green_light_count))
                if self.data_model_copy.left_Green_light_count <= 3:
                    if self.data_model_copy.left_Green_light_count % 2 == 0:
                        # print("绿")
                        self.left_light_twinkle()
                    else:
                        # print("黄")
                        self.left_light_twinkle_two()
            self.data_model_copy.left_Green_light_count -= 1

            if self.data_model_copy.left_Green_light_count == 0:
                if self.data_model_copy.left_Green_light_count % 2 == 0:
                    # print("绿")
                    self.left_light_twinkle()
                else:
                    # print("黄")
                    self.left_light_twinkle_two()
                self.left_light_label.setText("左灯运行：" + str(self.data_model_copy.left_Green_light_count))
                self.left_lightbox.setText("左灯还有：" + "0")

                self.data_model_copy = copy.copy(self.data_model)

                # print("left_over")

    def Refresh_mid_light_time(self):
        if self.data_model_copy.mid_light_count >= 0:
            # print("self.data_model_copy.mid_light_count", self.data_model_copy.mid_light_count)
            self.mid_lightbox.setStyleSheet("color:white;\n""background-color:rgb(255,0,0)")
            self.mid_light_label.setText("运行了：" + str(self.data_model_copy.mid_light_count))
            self.mid_lightbox.setText("中灯还有：" + str(self.data_model_copy.mid_light_count))
            if self.data_model_copy.mid_light_count <=3 :
                if self.data_model_copy.mid_light_count % 2 ==0:
                    self.mid_light_twinkle()
                else:
                    self.mid_light_twinkle_two()
            self.data_model_copy.mid_light_count -= 1
        else:
            if self.data_model_copy.mid_Green_light_count >0:
                self.mid_lightbox.setStyleSheet("color:white;\n""background-color:rgb(0,255,0)")
                self.mid_light_label.setText("中灯运行：" + str(self.data_model_copy.mid_Green_light_count))
                self.mid_lightbox.setText("中灯还有：" + str(self.data_model_copy.mid_Green_light_count))
                if self.data_model_copy.mid_Green_light_count <= 3:
                    if self.data_model_copy.mid_Green_light_count % 2 == 0:
                        # print("绿")
                        self.mid_light_twinkle()
                    else:
                        # print("黄")
                        self.mid_light_twinkle_two()
            self.data_model_copy.mid_Green_light_count -= 1

            if self.data_model_copy.mid_Green_light_count == 0:
                if self.data_model_copy.mid_Green_light_count % 2 == 0:
                    # print("绿")
                    self.mid_light_twinkle()
                else:
                    # print("黄")
                    self.mid_light_twinkle_two()
                self.mid_light_label.setText("中灯运行：" + str(self.data_model_copy.mid_Green_light_count))
                self.mid_lightbox.setText("中灯还有：" + "0")

                self.data_model_copy = copy.copy(self.data_model)

                # print("mid_over")
    def Refresh_right_light_time(self):
        if self.data_model_copy.right_light_count >= 0:
            # print("self.data_model_copy.mid_light_count", self.data_model_copy.mid_light_count)
            self.right_lightbox.setStyleSheet("color:white;\n""background-color:rgb(255,0,0)")
            self.right_light_label.setText("运行了：" + str(self.data_model_copy.right_light_count))
            self.right_lightbox.setText("中灯还有：" + str(self.data_model_copy.right_light_count))
            if self.data_model_copy.right_light_count <=3 :
                if self.data_model_copy.right_light_count % 2 ==0:
                    self.right_light_twinkle()
                else:
                    self.right_light_twinkle_two()
            self.data_model_copy.right_light_count -= 1
        else:
            if self.data_model_copy.right_Green_light_count >0:
                self.right_lightbox.setStyleSheet("color:white;\n""background-color:rgb(0,255,0)")
                self.right_light_label.setText("中灯运行：" + str(self.data_model_copy.right_Green_light_count))
                self.right_lightbox.setText("中灯还有：" + str(self.data_model_copy.right_Green_light_count))
                if self.data_model_copy.right_Green_light_count <= 3:
                    if self.data_model_copy.right_Green_light_count % 2 == 0:
                        # print("绿")
                        self.right_light_twinkle()
                    else:
                        # print("黄")
                        self.right_light_twinkle_two()
            self.data_model_copy.right_Green_light_count -= 1

            if self.data_model_copy.right_Green_light_count == 0:
                if self.data_model_copy.right_Green_light_count % 2 == 0:
                    # print("绿")
                    self.right_light_twinkle()
                else:
                    # print("黄")
                    self.right_light_twinkle_two()
                self.right_light_label.setText("中灯运行：" + str(self.data_model_copy.right_Green_light_count))
                self.right_lightbox.setText("中灯还有：" + "0")

                self.data_model_copy = copy.copy(self.data_model)

                # print("right_over")

    def left_light_twinkle(self):
        # print("hong ")
        self.left_lightbox.setStyleSheet("color:white;\n""background-color:rgb(255,0,0)")
        # 这个位置不行  闪烁变红
        # self.left_lightbox.setStyleSheet("color:white;\n""background-color:rgb(255,0,0)")
    def left_light_twinkle_two(self):
        # print("黄")
        #   这一行没有生效
        self.left_lightbox.setStyleSheet("color:white;\n""background-color:rgb(255,255,0)")

    def mid_light_twinkle(self):
        # print("hong ")
        self.mid_lightbox.setStyleSheet("color:white;\n""background-color:rgb(255,0,0)")
        # 这个位置不行  闪烁变红
        # self.left_lightbox.setStyleSheet("color:white;\n""background-color:rgb(255,0,0)")
    def mid_light_twinkle_two(self):
        # print("黄")
        #   这一行没有生效
        self.mid_lightbox.setStyleSheet("color:white;\n""background-color:rgb(255,255,0)")

    def right_light_twinkle(self):
        # print("hong ")
        self.right_lightbox.setStyleSheet("color:white;\n""background-color:rgb(255,0,0)")
        # 这个位置不行  闪烁变红
        # self.left_lightbox.setStyleSheet("color:white;\n""background-color:rgb(255,0,0)")
    def right_light_twinkle_two(self):
        # print("黄")
        #   这一行没有生效
        self.right_lightbox.setStyleSheet("color:white;\n""background-color:rgb(255,255,0)")

# 传参   rg 是true   就是绿灯     就是闪烁           twinkle
#  255  255  0   是黄色
#  255  0    0   是红色
#  0    255  0   是绿色
# last_twinkle  没定义
    def left_light_Action(self,rg,twinkle):
        # print("黄")
        #   这一行没有生效
        self.last_twinkle == False
        if twinkle == True:
            if self.last_twinkle ==False:
                print("jinru!!!!!!!!!!!!")
                self.left_lightbox.setStyleSheet("color:white;\n""background-color:rgb(255,255,0)")
                self.last_twinkle = True
            else:
                if rg == True:
                    self.left_lightbox.setStyleSheet("color:white;\n""background-color:rgb(0,255,0)")
                else:
                    self.left_lightbox.setStyleSheet("color:white;\n""background-color:rgb(255,0,0)")
                self.last_twinkle = False

# 无传参   curr_light_style_flag  绿灯？
#
    def time_loop_for_lght(self):
        self.curr_light_style_flag = True
        self.running_time = 10

        self.running_time -=1

        if self.running_time >=0:
            rg = self.curr_light_style_flag
            twinkle = self.running_time<3
            self.left_light_Action(rg,twinkle)
        else:
            if self.curr_light_style_flag:
                self.running_time = self.data_model_copy.left_Green_light_count
                self.curr_light_style_flag=  False
            else:
                self.running_time = self.data_model_copy.left_light_count
                self.curr_light_style_flag=  True

    def Action_submission(self):
        self.data_model.left_light_count = int(self.change_left_red.toPlainText())
        self.data_model.mid_light_count = int(self.change_mid_red.toPlainText())
        self.data_model.right_light_count = int(self.change_right_red.toPlainText())
        self.data_model.left_Green_light_count = int(self.change_left.toPlainText())
        self.data_model.mid_Green_light_count = int(self.change_mid.toPlainText())
        self.data_model.right_Green_light_count = int(self.change_right.toPlainText())
        # self.info = [self.data_model_copy.left_light_count, self.data_model_copy.mid_light_count,self.data_model_copy.right_light_count]
        self.data_model_copy = copy.copy(self.data_model)
        # self.data_model_copy=self.data_model
        # print(self.info)
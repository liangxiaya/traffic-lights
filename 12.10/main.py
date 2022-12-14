from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import sys
import time
# class Ui_Dialog(object):
from PyQt5.QtWidgets import QApplication, QWidget , QVBoxLayout , QListView, QMessageBox
from PyQt5.QtCore import QStringListModel
import mainmain
from basic_model import Basic_function
class Ui_Dialog(QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(618, 479)
        self.data_model = Basic_function(10, 20, 10);
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
        # --------------------  1.7  4???  ??????????????????
        self.shuxing = QtWidgets.QLabel(Dialog)
        self.shuxing.setGeometry(QtCore.QRect(340, 250, 81, 41))
        self.shuxing.setObjectName("shuxing")
        self.change_left = QtWidgets.QTextEdit(Dialog)
        self.change_left.setGeometry(QtCore.QRect(420, 260, 101, 31))
        self.change_left.setObjectName("change_left")
        self.change_mid = QtWidgets.QTextEdit(Dialog)
        self.change_mid.setGeometry(QtCore.QRect(420, 300, 101, 31))
        self.change_mid.setObjectName("change_mid")
        self.change_right = QtWidgets.QTextEdit(Dialog)
        self.change_right.setGeometry(QtCore.QRect(420, 340, 101, 31))
        self.change_right.setObjectName("change_right")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(540, 280, 51, 41))
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)  # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject)  # type: ignore
        self.pushButton.clicked.connect(Dialog.close)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # --------------------  1.7  4???  ??????????????????

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.start_box.setText(_translate("Dialog", "start"))
        self.left_light_label.setText(_translate("Dialog", "???????????????"))
        self.pushButton.setText(_translate("Dialog", "????????????"))
        self.zanting_box.setText(_translate("Dialog", "??????"))
        self.mid_light_label.setText(_translate("Dialog", "???????????????"))
        self.left_lightbox.setText(_translate("Dialog", "?????????0???"))
        self.comboBox.setItemText(0, _translate("Dialog", "??????"))
        self.comboBox.setItemText(1, _translate("Dialog", "??????"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "??????"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "??????"))
        self.mid_lightbox.setText(_translate("Dialog", "?????????0???"))
        self.right_lightbox.setText(_translate("Dialog", "?????????0???"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "??????"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "??????"))
        self.comboBox_4.setItemText(0, _translate("Dialog", "???"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "??????"))
        self.comboBox_5.setItemText(0, _translate("Dialog", "??????"))
        self.comboBox_6.setItemText(0, _translate("Dialog", "???"))
        self.comboBox_6.setItemText(1, _translate("Dialog", "??????"))
        self.comboBox_6.setItemText(2, _translate("Dialog", "??????"))
        self.right_light_label.setText(_translate("Dialog", "???????????????"))

    def Action(self):
        if self.start_box.isEnabled():
            self.reduce_time.start()
            print("????????????if??????")

    def Action_stop(self):
        print("time stop")
        self.reduce_time.stop()

    # def Action_left_light_time(self):
    #     self.ui.start
    # def Action_left_red(self):
    #     print("111111111111111111111111111")
    def reduce_time(self):
        totalTime = 5
        if totalTime.isdigit():
            print(totalTime)
            totalTime = int(totalTime)
            while totalTime > 0:
                print('??????%d???' % totalTime)
                time.sleep(1)
                totalTime -= 1
            print("?????????")
        else:
            print("???????????????")
        return 0

    def Refresh_light_time(self):
        # self.left_light_label.setProperty("value", str(self.main.value_of_hunger))
        print("???????????????????????????")
        if self.data_model.redlight_count > 0:
            # self.left_light_label.setProperty("value", str(self.data_model.redlight_count))
            print(self.data_model.redlight_count)
            # setProperty????????????   settext  ??????+?????? ??????
            self.lights_count = 1
            self.left_light_label.setText("??????????????????" + str(self.lights_count))
            self.lights_count += 1
            # 1.7??????
            self.left_lightbox.setText("???????????????" + str(self.data_model.redlight_count))
            self.data_model.redlight_count -= 1
        else:
            self.reduce_time.stop()
            print("over")
        # ------------------------????????????0  ??????????????????

    def Refresh_water(self):
        self.left_light_label.setProperty("value", str(self.main.redlight_count))
        print("jinru ")
        # self.mid_light_label.setProperty("value", str(self.mainmain.redlight_count))
        # if self.water_count > 0:
        #     # self.start.setText(str(self.count) + '???')
        #     self.water_Bar.setProperty("value", str(self.mainmain.value_of_water))
        #     if self.mainmain.value_of_water < 45:  # ????????????
        #         print("WARING")
        #         self.list.append("WARING")
        #     # main.Basic_function.changed_hunger(main.Basic_function.value_of_hunger)
        #     # self.pushButton_3.setText("????????????",self.count)
        #     self.label_2.setText("????????????" + str(self.mainmain.value_of_water))
        #     print("water????????????" + str(self.water_count) + '???')
        #
        #     self.water_count -= 1
        #     self.pushButton_4.setText("????????????" + str(self.water_count))
        #
        #     # if self.count == 0:
        #     #     self.changed_water()
        # else:
        #     # self.Action_stop()
        #     self.water_time.stop()
        #     self.list.append(self.info)
        #     self.info = ["?????????:" + str(self.mainmain.value_of_hunger), "?????????" + str(self.mainmain.value_of_water)]
        #
        self.left_light_label.setText("????????????" + str(self.mainmain.redlight_count))
        print("red????????????" + str(self.redlight_count) + '???')
        # print("????????????" + str(self.mainmain.value_of_hunger))
        # print("????????????" + str(self.mainmain.value_of_water))
        # self.journal.setText(str(self.list))  # ?????????
        # self.pushButton_4.setText("????????????" + str(self.water_count))
        # self.mainmain.changed_water(self.mainmain.value_of_water)
        # self.label_2.setText("????????????" + str(self.mainmain.value_of_water))
        # # self.changed_water()
        # # self.start.setEnabled(True)
        # self.start.setText('??????')
        # self.water_Bar.setProperty("value", str(self.mainmain.value_of_water))
        # # self.count = 10
        # self.water_count = 5  # ??????
        # self.water_time.start()
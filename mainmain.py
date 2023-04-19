import sys
import time
import datetime
import os
# from PyQt5.QtCore import QObject , pyqtSignal
# import msvcrt
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
# from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import QMainWindow, QPushButton , QWidget , QMessageBox, QApplication, QDialog,QHBoxLayout
import sys
import untitled_new

class Basic_function:
    def __init__(self,value_of_hunger, value_of_water):
        # 初始化属性设置
        self.value_of_hunger = value_of_hunger
        self.value_of_water = value_of_water
        self.reduce_hunger=2
        self.reduce_water=2

    def get_descriptive_info(self):
        # 返回属性值
        #     info = f'饥饿值：{self.value_of_hunger}\n水份：{self.value_of_water}'

        info = [self.value_of_hunger,self.value_of_water]
        print(info)

        # print("饥饿值: ", info['self.value_h'])
        # print("口渴值: ", info['self.value_w'])
        # time.sleep(3)
        return info


    def changed_hunger(self, value_of_hunger):
        #将读数递减
            time.sleep(1)
            self.value_of_hunger = self.value_of_hunger-self.reduce_hunger
            print(value_of_hunger)
            return self.value_of_hunger

    # if self.value_of_hunger == 0:

    def changed_water(self, value_of_water):
            time.sleep(1)
            self.value_of_water =self.value_of_water-self.reduce_hunger
            if value_of_water < 0:
                value_of_water = 0
                # print(a.value_of_water)
                print("由于口渴值为0  口渴而死")
                sys.exit(0)
                # break
            return self.value_of_water

            # if self.value_of_water == 0:
    def local_time(self):
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
        now2 = time.strftime("%Y-%m-%d", time.localtime())
        print(now)
        print(now2)
        #获取系统时间
#---------------------------------------------------------测试绑定函数
# class WinForm(QMainWindow):
#     def __init__(self, parent=None):
#         super(WinForm, self).__init__(parent)
#         button1 = QPushButton('饥饿值更改')               #创建按钮
#         button2 = QPushButton('口渴值更改')
#
        # 将信号连接到指定槽函数
        #
        # button1.clicked.connect(lambda: self.WinForm_change_hunger)
        # button2.clicked.connect(lambda: self.WinForm_change_water)
        #
        # layout = QHBoxLayout()                      #水平布局
        # layout.addWidget(button1)                   #往布局中添加控件
        # layout.addWidget(button2)
        #
        # main_frame = QWidget()                      #创建窗口
        # main_frame.setLayout(layout)                #把布局塞进去
        # self.setCentralWidget(main_frame)           #设置成中心部件
    #
    # def WinForm_change_hunger(self, n):
    #     a.changed_hunger(hunger)
    #     hunger - reduce_hunger
    #     print("正在饥饿中")
    #     return a.value_of_hunger
    #
    # def WinForm_change_water(self):
    #     a.changed_water(water)
    #     water - reduce_water
    #     print("正在口渴中")
    #     return a.value_of_water
#


if __name__ == "__main__":

    app = QApplication(sys.argv)
    MainWindow = QDialog()
    ui=untitled_new.Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# var = 1
#
# # while var ==1:
# # a.get_descriptive_info()
# # time.sleep(3)                                            调试关闭
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
#     # if a.value_of_water < 0:
#     #     a.value_of_water=0
#     #     print(a.value_of_water)
#     #     print("由于口渴而死")
#     #     # sys.exit(0)
#     #     break
#     # print(a.get_descriptive_info().info)
#
# # if a.value_of_water < 30:
# #      print("**我有点渴了**")
# #      time.sleep(1)
# # if a.value_of_hunger <30:
# #     print("**我有点饿了**")
# #     time.sleep(1)
# # if a.value_of_hunger <0:
# #     print("由于饥饿而死")
# # if a.value_of_water <0:
# #     print("由于口渴而死")
#
# sys.exit(app.exec_())

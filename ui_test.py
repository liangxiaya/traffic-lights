import ui
import sys
# from PyQt5.Qtwidgets import QtCore, QtGui, QtWidgets
from PyQt5 import *

# if __name__ == '__main__':
#     # # 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
#     # app = QtWidgets.QApplication(sys.argv)
#     # # QWidget部件是pyqt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类。
#     # w = QWidget()
#     # # resize()方法调整窗口的大小。这离是250px宽150px高
#     # w.resize(250, 150)
#     # # move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
#     # w.move(300, 300)
#     # # 设置窗口的标题
#     # w.setWindowTitle('Simple')
#     # # 显示在屏幕上
#     # w.show()
#     #
#     # # 系统exit()方法确保应用程序干净的退出
#     # # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
#     # sys.exit(app.exec_())
#     app =QApplication(sys.argv)
#     mainwindow = QMainWindow()
#     ui =Main

    # app = QtWidgets.QApplication(sys.argv)
    # mainWindow = QtWidgets.QMainWindow()
    # ui = MainWindow()
    # ui.setupUi(mainWindow)
    # mainWindow.show()
    # sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow
from PyQt5.QtGui import QIcon
import untitled_new


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    MainWindow = QDialog()
    ui=untitled.Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
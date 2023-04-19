import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ComboxDemo(QWidget):
    def __init__(self, parent=None):
        super(ComboxDemo, self).__init__(parent)
        self.setWindowTitle("combox 示例")
        self.resize(300, 90)
        layout = QVBoxLayout()
        self.lbl = QLabel("")

        self.cb = QComboBox()
        self.cb.addItem("C")
        self.cb.addItem("C++")
        self.cb.addItems(["Java", "C#", "Python"])
        self.cb.currentIndexChanged.connect(self.selectionchange)
        layout.addWidget(self.cb)
        layout.addWidget(self.lbl)
        self.setLayout(layout)

    def selectionchange(self, i):
        self.lbl.setText(self.cb.currentText())
        self.lbl.adjustSize()

        print("Items in the list are :")
        for count in range(self.cb.count()):
            # 打印出所有的下拉框索引和名称
            print('item' + str(count) + '=' + self.cb.itemText(count))
            print("Current index", i, "selection changed ", self.cb.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    comboxDemo = ComboxDemo()
    comboxDemo.show()
    sys.exit(app.exec_())

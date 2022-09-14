"""
这个例子中我们实现了两个功能：菜单按钮、带倒计时的按钮（账户注册的时候经常会碰到）。
"""
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMenu
from PyQt5.QtCore import QTimer
import sys
import time





class Example(QWidget):
    def __init__(self):
        # 初始化属性设置
        value_of_hunger=100
        value_of_water=100
        self.value_of_hunger = value_of_hunger
        self.value_of_water = value_of_water
        super().__init__()
        self.initUI()
        self.reduce_hunger = 2
        self.reduce_water = 3

    # def __init__(self, value_of_hunger, value_of_water):
    #     # 初始化属性设置
    #     self.value_of_hunger = value_of_hunger
    #     self.value_of_water = value_of_water
    #     super().__init__()
    #     self.initUI()
    #     water = 100
    #     hunger = 100
    #     reduce_hunger = 2
    #     reduce_water = 3

    def get_descriptive_info(self):
        # 返回属性值
        #     info = f'饥饿值：{self.value_of_hunger}\n水份：{self.value_of_water}'

        info = [self.value_of_hunger,self.value_of_water]
        print(info)

        # print("饥饿值: ", info['self.value_h'])
        # print("口渴值: ", info['self.value_w'])
        # time.sleep(3)
        return info


    def changed_hunger(self):
        #将读数递减
        self.value_of_hunger = self.value_of_hunger-self.reduce_hunger
        print(self.value_of_hunger)
        return self.value_of_hunger

    # if self.value_of_hunger == 0:

    def changed_water(self, value_of_water):
            time.sleep(1)
            self.value_of_water =self.value_of_water-self.reduce_water
            if self.value_of_water < 0:
                self.value_of_water = 0
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


    def initUI(self):
        self.resize(400,300)
        self.setWindowTitle('pet')  ##标题
        bt1 = QPushButton("这是什么",self)
        bt1.move(50,50)
        self.bt2 = QPushButton('开始',self)
        self.bt2.move(200,50)
        self.count = 10
        self.bt2.clicked.connect(self.Action)
        self.time = QTimer(self)
        self.time.setInterval(1000)
        self.time.timeout.connect(self.Refresh)

        self.show()
        """
我们单击按钮后，进行判断若按钮没有被禁用，则激活定时器，同时将按钮禁用，即禁止点击。
        """
    def Action(self):
        if self.bt2.isEnabled():
            self.time.start()
            self.bt2.setEnabled(False)
        """
进入超时状态后，我们开始倒计时。同时让按钮上的文字不断的在变化。
当倒计时完成的时候，我们停止定时器。将按钮恢复成正常的状态。同时重置倒计时的值，为下次的使用做好准备。 
        """
    def Refresh(self):
        if self.count > 0:
            self.bt2.setText(str(self.count)+'秒')
            # print(info)
            print(str(self.count)+'秒')
            self.count -= 1
        # if self.count == 0:
        #     self.changed_water()
        else:
            self.time.stop()
            self.changed_water()
            self.bt2.setEnabled(True)
            self.bt2.setText('开始')
            self.count = 10



print("**********start**********")
# a.local_time()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
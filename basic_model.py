class Basic_function:
    def __init__(self,left_light_count, midlight_count,rightlight_count):
        # 初始化属性设置
        # self.redlight_count = redlight_count
        self.left_light_count = left_light_count

        # self.greanlight_count = greanlight_count
        self.mid_light_count = midlight_count
        self.light_twinkle = 2

        # self.rightlight_count = rightlight_count
        self.right_light_count = rightlight_count

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
            # time.sleep(1)
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
    # def local_time(self):
    #     now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    #     now2 = time.strftime("%Y-%m-%d", time.localtime())
    #     print(now)
    #     print(now2)
    #     #获取系统时间
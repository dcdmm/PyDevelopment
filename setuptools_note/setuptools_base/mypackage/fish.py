import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)  # 利用构造方法定义属性
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print('🐟移动后的位置是', self.x, self.y)


class Goldfish(Fish):
    pass


class Shark0(Fish):
    def __init__(self):  # 重写了__init__方法(父类的__init__方法被覆盖)
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('吃货的梦想就是天天吃东西')
            self.hungry = False
        else:
            print('吃不下了')


class Shark1(Fish):
    def __init__(self):
        Fish.__init__(self)  # self是子类的实例对象
        self.hungry = False

    def eat(self):
        if self.hungry:
            print('吃货的梦想就是天天吃东西')
            self.hungry = False
        else:
            print('吃不下了')


class Shark2(Fish):
    def __init__(self):
        super().__init__()
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('吃货的梦想就是天天吃东西')
            self.hungry = False
        else:
            print('吃不下了')
# 面向过程编程
user1 = {'name': 'tom', 'hp': 100}
user2 = {'name': 'jerry', 'hp': 80}


def prit_role(user):
    print('name:%s  hp:%s' % (user['name'], user['hp']))


prit_role(user1)
prit_role(user2)


# 面向对象编程
class Player:  # 定义一个类
    def __init__(self, name, hp):
        self.__name = name  # 私有化属性，外部不可修改，只可通过方法修改
        self.hp = hp

    def print_player(self):  # 定义一个方法
        print('name:%s  hp:%s' % (self.__name, self.hp))

    def updateName(self, newName):
        self.__name = newName


tom = Player('tom', 100)  # 类实例化
jerry = Player('jerry', 80)
tom.print_player()
jerry.print_player()

tom.name = 'aaa'  # tom的name变成了aaa 防止这种情况，可以使用__私有化属性（类的封装）
tom.print_player()  # name:tom  hp:100

tom.updateName('BigTom')
tom.print_player()  # name:BigTom  hp:100


# 类的封装  使用私有属性  __

# 类的继承 封装 多态  type和 isinstance（）  可以得出谁是父类谁是子类

class Father:
    def __init__(self, hp=100):
        self.hp = hp

    def run(self):
        print("父类在跑")


class Son(Father):
    def __init__(self, hp=100):
        super().__init__(hp)

    def run(self):
        print("子类在跑")


fater1 = Father(30)
print(fater1.hp)
fater1.run()

son1 = Son(50)
print(son1.hp)
son1.run()

print(isinstance(son1, Father))


# 参数可变  * 表示非必输参数
def function(param1, *param):
    print(len(param1) + len(param))


function("1", '2', '3', '4', '5', '6', '7')

# global 全局变量
var1 = 123


def function1():
    global var1
    var1 = 456
    print(var1)


function1()
print(var1)


# 迭代器iter() 和生成器yield()   运行到到当前位置，暂定并记录当前位置，当再次调用next时候，通过当前位置返回一个值

def frange(start, stop, step):
    temp = start
    while temp <= stop:
        yield temp
        temp += step


for i in frange(10, 20, 0.5):
    print(i)

# lambda 表达式 省略方法名，省略return

lambda x, y: x + y


def add(x, y):
    return x + y


# filter()  筛选a中大于2的数
a = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda x: x > 2, a)))

# map()  把多个参数依次进行处理
c = [4, 5, 6]
d = [1, 2, 3]
print(list(map(lambda x: x + 1, d)))

print(list(map(lambda x, y: x + y, c, d)))

from functools import reduce

# reduce() 把序列和初始值按照函数的方式做运算 三个参数 函数 序列 初始值
e = [2, 3, 4]
init_value = 1
print(reduce(lambda x, y: x + y, e, init_value))  #--10


# zip() 转换
f = [1, 2, 3]
g = [4, 5, 6]
for i in zip(f, g):
    print(i)
# (1, 4)
# (2, 5)
# (3, 6)
dicth = {'a': "aa", 'b': "bb"}

print(dict(zip(dicth.values(), dicth.keys()))) #{'aa': 'a', 'bb': 'b'}‘



#闭包：外部函数变量被内部函数引用叫做闭包。


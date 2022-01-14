def sum(a):
    def add(b):
        return a + b

    return add


# add 函数名称或者函数引用
# add（） 函数调用

function_sum = sum(1)  # type为function
number = function_sum(2)  # type int
print(number)


# 实现一个计数器 每次加1
def counter(first=0):
    nt = [first]

    def count():
        nt[0] += 1
        return nt[0]

    return count


count_function5 = counter(5)
count_function10 = counter(10)
print(count_function5())
print(count_function5())
print(count_function10())
print(count_function10())


# 计算y=a*x+b
def a_line(a, b):
    def arg_x(x):
        return a * x + b

    return arg_x


# 使用lambda表达式
def a_line2(a, b):
    return lambda x: a * x + b


# 计算a=10 b=5
line_function = a_line(10, 5)
line_function_lambda = a_line2(10, 5)
print(line_function(3))
print(line_function_lambda(3))




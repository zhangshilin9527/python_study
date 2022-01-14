import time


# 装饰器与闭包不同点：1.装饰器参数为方法 2.调用更方便
# 不带参的装饰器
def timmer(function):
    def wrapper():
        start_time = time.time()
        function()
        end_time = time.time()
        print('方法使用%s秒' % (end_time - start_time))

    return wrapper


@timmer
def i_sleep():
    time.sleep(3)


i_sleep()


def function_sleep():
    start_time = time.time()
    i_sleep()
    end_time = time.time()
    print('方法使用%s秒' % (end_time - start_time))


function_sleep()


# 带参的装饰器
def tips(func):
    def nei(a, b):
        print("start %s" % func.__name__)
        func(a, b)
        print("end")

    return nei


@tips
def add(a, b):
    print(a + b)


@tips
def sub(a, b):
    print(a - b)


add(3, 4)
sub(4, 3)


def new_tips(arg):
    def tips(func):
        def nei(a, b):
            print("start %s" % arg)
            func(a, b)
            print("end")

        return nei

    return tips


@new_tips("add")
def add(a, b):
    print(a + b)


@new_tips("sub")
def sub(a, b):
    print(a - b)


add(3, 4)
sub(4, 3)

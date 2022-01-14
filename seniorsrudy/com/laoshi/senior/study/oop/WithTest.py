class TestWith:
    def __enter__(self):  # 使用with时候初始化执行方法
        print("初始化方法")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出方法")  # 使用with时候退出执行方法
        if exc_tb is None:  # exc_tb  is None 表示有异常
            print("没有异常")
        else:
            print('出现异常%s' % exc_tb)


with TestWith():  # with后面需要带括号
    print("开始执行")
    print("开始执行")
    print("开始执行")
    raise NameError("出现名称异常")



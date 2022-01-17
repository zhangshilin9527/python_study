# while 表达式：
#     代码块
import time

num = 0
while True:
    print("a")
    num = num + 1
    if num > 10:
        break
numa = 0
while True:
    numa = numa + 1
    if numa == 10:
        continue  # 不会输出10
    print(numa)
    time.sleep(1)

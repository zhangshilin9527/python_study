import threading
from threading import current_thread


def myThread(arg1, arg2):
    print(current_thread().name, 'start')
    print(arg1, arg2)
    print(current_thread().name, 'end')


# # 单线程
# for i in range(1, 6, 1):
#     myThread(i, i + 1)

# 多线程
for i in range(1, 6, 1):
    t1 = threading.Thread(target=myThread, args=(i, i + 1))
    t1.start()
print(current_thread().name, 'stop')

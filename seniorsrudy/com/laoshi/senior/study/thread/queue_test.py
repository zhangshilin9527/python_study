import random
import time
from queue import Queue
from threading import Thread, current_thread

queue = Queue(5)


class ProductThread(Thread):
    def run(self):
        name = current_thread().name  # 获取当前线程名称
        nums = range(100)  # 从1到100
        global queue
        while True:
            num = random.choice(nums)  # 从1到100选一个数
            queue.put(num)  # 放入队列
            print('生产者 %s 产生了数据 %s' % (name, num))
            t = random.randint(1, 3)  # 从1到3随机产生1个数
            time.sleep(t)  # 休眠t秒
            print('生产者 %s 睡眠了 %s 秒' % (name, t))


class ConsumerThread(Thread):

    def run(self):
        name = current_thread().name
        global queue
        while True:
            num = queue.get()
            queue.task_done()  # 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
            print('消费者 %s 消费了数据 %s' % (name, num))
            t = random.randint(1, 3)  # 从1到3随机产生1个数
            time.sleep(t)  # 休眠t秒
            print('消费者 %s 睡眠了 %s 秒' % (name, t))


product1 = ProductThread()
product1.start()
product2 = ProductThread()
product2.start()
consumer1 = ConsumerThread()
consumer1.start()


import threading
from threading import current_thread


class myThread(threading.Thread):
    def run(self):
        print(current_thread().name, 'start')
        print('run')
        print(current_thread().name, 'end')


t1 = myThread()
t1.start()
t1.join()

print(current_thread().name, 'stop')

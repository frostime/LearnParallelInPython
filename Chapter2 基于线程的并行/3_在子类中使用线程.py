# -*- coding: utf-8 -*-
"""
继承threading.Thread构造一个线程类
重写类的run方法
一旦开始start，就会执行run方法
"""
import threading as td
import time


exit_flag = 0


class MyThread(td.Thread):
    def __init__(self, threadId, name, delay):
        super().__init__()
        self.threadId = threadId
        self.name = name
        self.delay = delay

    def run(self):
        print('Starting' + self.name)
        printTime(self.name, self.delay, 5)
        print('Exiting' + self.name)


def printTime(name, delay, cnt):
    while cnt:
        if exit_flag:
            td.exit()
        time.sleep(delay)
        print('{}: {}'.format(name, time.ctime(time.time())))
        cnt -= 1


def main():
    t1 = MyThread(1, 'T-1', 1)
    t2 = MyThread(2, 'T-2', 2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('Exit Main Thread')


if __name__ == '__main__':
    main()

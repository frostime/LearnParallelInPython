# -*- coding: utf-8 -*-
"""
RLock和Lock大致相似，但是有一个决定性的不同之处
RLock可以多次acquire而Lock不可以，也就是说:
>>> lock = threading.Lock()
>>> lock = threading.RLock()
>>> # No
>>> lock.acquire()
>>> lock.acquire()
>>> # OK
>>> lock.acquire()
>>> lock.acquire()

但是要注意，acquire必须和release成对出现

RLock在同一个线程反复加锁的时候很有用，最典型的例子就是递归

本文件的代码中，在Box中使用RLock，如果换成Lock，就会发生死锁
"""
import threading as td
from threading import Thread
import time


SLEEP = 0.1


class Box(object):
    # 不可以用Lock，不然会死锁
    # lock = td.Lock()
    lock = td.RLock()
    def __init__(self):
        self.total_items = 0

    def execute(self, n):
        Box.lock.acquire()
        self.total_items += n
        Box.lock.release()

    def add(self):
        Box.lock.acquire()
        self.execute(1)
        Box.lock.release()

    def remove(self):
        Box.lock.acquire()
        self.execute(-1)
        Box.lock.release()


def add(box, items):
    for _ in range(items):
        print('Add 1 item in the box')
        box.add()
        time.sleep(SLEEP)


def remove(box, items):
    for _ in range(items):
        print('Remove 1 item in the box')
        box.remove()
        time.sleep(SLEEP)


def main():
    items = 5
    print('Put {} items in the box'.format(items))
    box = Box()
    t1 = Thread(target=add, args=(box, items))
    t2 = Thread(target=remove, args=(box, items))
    t1.start()
    t2.start()
    t1.join()
    t1.join()
    print('{} items still in box'.format(box.total_items))


if __name__ == '__main__':
    main()

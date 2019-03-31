# -*- coding: utf-8 -*-
# pylint: disable=global-statement
"""
使用Lock来完成线程同步问题:
假定有一个资源: x = 0. 有两个线程分别对它进行加一和减一的操作
分别来看一看在使用和不使用Lock两种情况下的结果.

这里由于比较简单，暂时不涉及死锁的问题

原书中的代码看不出效果，所以稍微改动了一下，变成了:
temp = shared_resouce
time.sleep(SLEEP)
shared_resouce = temp ± 1

这样更能模拟出大规模IO操作中容易出现的问题
"""
import threading as td
import time


shared_resouce_with_lock = 0
shared_resouce_without_lock = 0
COUNT = 1000
SLEEP = 0.001

lock = td.Lock()


def incWithLock():
    global shared_resouce_with_lock
    for _ in range(COUNT):
        lock.acquire()
        temp = shared_resouce_with_lock
        time.sleep(SLEEP)
        shared_resouce_with_lock = temp + 1
        lock.release()


def incWithoutLock():
    global shared_resouce_without_lock
    for _ in range(COUNT):
        temp = shared_resouce_without_lock
        time.sleep(SLEEP)
        shared_resouce_without_lock = temp + 1


def decWithLock():
    global shared_resouce_with_lock
    for _ in range(COUNT):
        lock.acquire()
        temp = shared_resouce_with_lock
        time.sleep(SLEEP)
        shared_resouce_with_lock = temp - 1
        lock.release()


def decWithoutLock():
    global shared_resouce_without_lock
    for _ in range(COUNT):
        temp = shared_resouce_without_lock
        time.sleep(SLEEP)
        shared_resouce_without_lock = temp - 1


def main():
    # 使用锁
    t1 = td.Thread(target=incWithLock)
    t2 = td.Thread(target=decWithLock)
    # 不使用
    t3 = td.Thread(target=incWithoutLock)
    t4 = td.Thread(target=decWithoutLock)
    # 开始
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    # 结果
    print('shared_resouce_with_lock = ', shared_resouce_with_lock)
    print('shared_resouce_without_lock = ', shared_resouce_without_lock)


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""
使用threading.currentThread可以知道当前的线程
使用name参数可以对线程命名
注意到print('---|\n|---')执行到一半就跳转了
"""
import threading as td
import time


def fun():
    cur_thread = td.currentThread()
    print(cur_thread.getName() + ' is Starting')
    print('---|\n|---')
    time.sleep(2)
    print(cur_thread.getName() + ' is Exiting')


def main():
    t1 = td.Thread(target=fun, name='Thread 1st')
    t2 = td.Thread(target=fun, name='Thread 2nd')
    t3 = td.Thread(target=fun)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()


if __name__ == '__main__':
    main()

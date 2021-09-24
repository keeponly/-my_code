# @Time     :2020/10/17  14:55
# @Author   :wang-kai
# @tel      :15313929271
# @File    :进程.py
"""一个进程里面至少包含一个线程,进程操作系统分配资源的最小单位 ,系统分配的资源,进程有多个线程
     进程全局变量不共享"""
# 创建进程
import time
from multiprocessing import Process


def fun():
    for i in range(5):
        print('这是任务一')
        time.sleep(1)


def fun1():
    for i in range(100):
        print('这是任务二')
        time.sleep(1)


if __name__ == '__main__':
    p1 = Process(target=fun)
    p2 = Process(target=fun1)
    p1.start()
    p2.start()
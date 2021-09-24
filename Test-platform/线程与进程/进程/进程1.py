# @Time     :2020/10/17  17:25
# @Author   :wang-kai
# @tel      :15313929271
# @File    :进程1.py
# 多进程如何处理同一个变量,因为多进程不能共用一个内存,所以不能公用一个队列
from multiprocessing import Process, Queue
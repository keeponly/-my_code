# @Time     :2020/10/13  22:47
# @Author   :wang-kai
# @tel      :15313929271
# @File    :线程03.py


import threading


a = 100


def func():
    for i in range(100000):
        global a
        a += 1
    print('wang{}'.format(a))


def func1():
    for i in range(100000):
        global a
        a += 1
    print('kai{}'.format(a))


t1 = threading.Thread(target= func)
t2 = threading.Thread(target= func1)
t1.start()
t2.start()
t1.join()
t2.join()
print('tuu', a)


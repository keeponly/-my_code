# @Time     :2020/10/12  22:38
# @Author   :wang-kai
# @tel      :15313929271
# @File    :线程.py
import time
import threading


def func():
    for i in range(5):
        print(2)
        time.sleep(1)


def func1():
    for i in range(10):
        print(3)
        time.sleep(1)


def main():
    t1 = threading.Thread(target=func)
    t2 = threading.Thread(target=func1)
    s = time.time()
    t1.start()
    t2.start()
    print(threading.enumerate())  # 活动线程
    print(threading.active_count())  # 活动线程的个数
    t1.join()  # 线程不运行结束,不会运行下面的代码
    t2.join()
    e = time.time()
    print(5555)
    print(e - s)


if __name__ == '__main__':
    main()

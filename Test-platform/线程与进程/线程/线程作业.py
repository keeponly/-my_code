# _*_coding: utf-8 _*_
# @Time     :2020/10/14  9:31
# @Author   :wangkai
# @tel      :153139292711
# @ File    :线程作业.py 

"""创建一个线程类，每个线程对应地址url 发送100个请求，开启是个线程，同时发送，计算总耗时，分析平均每个请求所需时间 """
import time

import requests
import threading


class ThreadRequests(threading.Thread):
    def run(self):
        for i in range(100):
            res = requests.get('http://httpbin.org/post')
            print('Thread-{}---第{}次请求'.format(self.name,i+1))


def main():
    s = time.time()
    # 创建10个线程对象
    th = [ThreadRequests() for j in range(10)]
    # 遍历线程对象
    for i in th:
        i.start()
    for j in th:
        j.join()
    e = time.time()
    print('平均时间：{}'.format((e-s)/1000))


main()
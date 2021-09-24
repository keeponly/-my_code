# @Time     :2020/10/13  21:46
# @Author   :wang-kai
# @tel      :15313929271
# @File    :线程02.py
import threading

# 通过继承thread类来创建进程
import time

import requests


class RequestThread(threading.Thread):
    def __init__(self, url):
        self.url = url
        super().__init__()

    # 发送请求
    def run(self):
        res = requests.get(self.url)
        print('进程:{}----返回状态码{}'.format(threading.current_thread(), res.status_code))


s = time.time()
for i in range(5):
    t = RequestThread('http://www.baidu.com')
    t.start()
    e = time.time()
    print('耗时', e-s)



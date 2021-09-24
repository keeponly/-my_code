# _*_coding: utf-8 _*_
# @Time     :2020/10/30  11:05
# @Author   :wang_kai
# @tel      :153139292711
# @ File    :flask-44-可插拔试图.py
"""
method 定义支持的请求方式
dispatch_request 分配请求
decorators = [superuser_required] 装饰器
"""
from flask import Flask, request
from flask.views import View
app = Flask(__name__)

class MyView(View):
    methods = ['GET','POST']

    def dispatch_request(self):
        return 'Hello {}!'.format(request.methods)


app.add_url_rule('/hello/<name>', view_func=MyView.as_view('user'))
if __name__ == '__main__':
    app.run()
# @Time     :2020/10/29  21:12
# @Author   :wang-kai
# @tel      :15313929271
# @File    :flask-43-1.py
"""
路由 url 试图函数的绑定关系
map
app.route('/case',method=['POST'])
"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return '123'

# redirect_to重定向,不会去执行视图函数
# 默认参数 defaults = {'id':3}
# def case(id=None)


@app.route('/case', endpoint='case', redirect_to='/')  # endpoint 用于url和视图函数之间的桥梁
def case():
    return 'case'


if __name__ == '__main__':
    app.run(debug=True)
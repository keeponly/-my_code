# coding=utf-8
# @Time     :2020/10/22  22:11
# @Author   :wang-kai
# @tel      :15313929271
# @File    :flask-42.集中制.py
from flask import Flask


app = Flask(__name__)


def home():
    return '123'


app.add_url_rule('/', view_func=home)

if __name__ == '__main__':
    app.run(debug=True)
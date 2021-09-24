# _*_coding: utf-8 _*_
# @Time     :2020/10/22  16:46
# @Author   :wangkai
# @tel      :153139292711
# @ File    :flask-42.py 

from flask import Flask, request, render_template, config


app = Flask(__name__)


@app.route('/case', methods=['GET'])
def index():
    # 地址问号后面的,<int:id> http://127.0.0.1:5000/case?id=77
    id = request.args.get('id')
    return id   # f相当于format


"""/case与/case/两个不同的url   case/输入case可以访问   case/访问case不能访问
308重定向
"""


if __name__ == '__main__':

    app.run(debug=True)
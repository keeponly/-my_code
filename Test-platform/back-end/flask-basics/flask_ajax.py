# @Time     :2020/9/30  16:22
# @Author   :wang-kai
# @tel      :15313929271
# @File    :flask_ajax.py

from flask import Flask, jsonify
from flask import request
from project_path import html_path, css_path

uesr_info = {'user': 'wangkai', 'pwd':123}
app = Flask(__name__,
            template_folder=html_path,
            static_folder=css_path)


@app.route('/login', methods=['GET'])
def login():
    date = request.form
    print(date.get('user'))
    if uesr_info.get('user') == date.get('user') and uesr_info.get('pwd') == date.get('pwd'):
        return jsonify({'code': '1', 'data': None, 'msg': 'succeed'})
    else:
        return jsonify({'code': '0', 'data': None, 'msg': 'failed'})


if __name__ == '__main__':
    app.run()
# _*_coding: utf-8 _*_
# @Time     :2020/12/1  20:11
# @Author   :wangkai
# @tel      :153139292711
# @ File    :flask-43-2.py 

from flask import Flask,request,render_template

from project_path import html_path, css_path
# 初始化app
app = Flask(__name__,
            template_folder=html_path,
            static_folder=css_path)
@app.route('/uploads', methods=['GET','POST'])
def upload():
    if request.method == 'GET':
        return  render_template('index.html')
    if request.method =='POST':
        return 'success'

if __name__ == '__main__':
    app.run(debug=True)
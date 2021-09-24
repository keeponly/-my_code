# @Time     :2020/9/22  13:13
# @Author   :wang-kai
# @tel      :15313929271
# @File     :flask_01

from flask import Flask, request, render_template, config
from project_path import html_path, css_path
# 初始化app
app = Flask(__name__,
            template_folder=html_path,
            static_folder=css_path)
# 配置
app.config['DEBUG'] = True
app.config['PORT'] = 5002

# 必须返回视图函数本身的返回值，return返回的直接是以得相应，等于函数index的return，返回hello.则代表index return hello
def home(f):
    def deccorator(*args, **kw):
        return f(*args, **kw)
    return deccorator


# 添加路由
@app.route('/')
@home  # 装饰函数必须放在route里面
# 视图函数
def index():
    # 1.接收参数
    # 2.调用对应函数处理数据
    # 3.构建响应结果
    # args = request.args
    # name = args.get('username')
    # print(name)
    return render_template('home_page.html')


# 运行服务器
if __name__ == '__main__':
    app.run(port=app.config['PORT'], debug=app.config['DEBUG'])
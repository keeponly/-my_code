# @Time     :2020/4/27  16:14
# @Author   :wang-kai
# @tel      :15313929271
# @ File    :装饰器.py

username = 'wk'
password = '123456'


def login(func):
    def fun():
        user = input('输入用户名')
        pwd = input('输入密码')
        if user == username and pwd == password:
            func()
        else:
            print('用户名密码错误')
    return fun


@login
def index():
    print("网站登录成功")


index()
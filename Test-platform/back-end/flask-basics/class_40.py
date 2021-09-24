# @Time     :2020/9/10  23:01
# @Author   :wang-kai
# @tel      :15313929271
# @File    :class_40.py
"""
1.搭建服务
2.监听动作
3.处理程序
4.返回数据，生成一个响应对象
"""
import json
from wsgiref.simple_server import make_server


def home(request):
    return request


def login(request):
    return 'login'


# 路由
patterns = {
    '/': home,
    '/login': login
}


def app(env, start_response):
    # 状态码
    # env 获取请求相关数据 content请求格式，文本格式
    # 如果出现很多 ==的条件判断用字典去封装
    #  QUERY_STRING为地址里面的参数 PATH_INFO为请求地址
    url = env.get('PATH_INFO')
    param = env.get('QUERY_STRING')
    if url is None or url not in patterns.keys():
        msg = json.dumps({'msg': 'page not found'})
        start_response('404 not found', [('content-type', 'text/plain')])
        return [msg.encode()]
    start_response('200 ok', [('content-type', 'text/plain')])
    resp = patterns.get(url)
    if resp is None:
        start_response('404 not found', [('content-type', 'text/plain')])
        return [b'page not found']

    return [resp(param).encode()]


server = make_server("", 6001, app)
server.serve_forever()

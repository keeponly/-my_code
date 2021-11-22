# -*-coding:utf-8-*-
# @time     :2019/4/30 14:43
# Author    :lemon_youran
# @Email    :1063699580@qq.com
# @File     :http_requests.PY
# @Software :PyCharm
import requests
import json
class HttpRequests:
    """该类完成http的post,get请求，并返回结果"""
    def http_request(self, method, url, param,headers=None,verify=False):
        """根据请求方式来确定发起get请求，还是post请求
        url 发送请求的接口地址
        method 请求方式
        param请求参数"""
        if method.upper() == 'GET':
            try:
                resp = requests.get(url, params=param,headers=headers,verify=verify)
            except Exception as e:
                print("get请求时出错了：{}".format(e))
        elif method.upper() == 'POST':
            print(param)
            try:
                resp = requests.post(url,data=param,headers=headers,verify=verify)

            except Exception as e:
                print("post请求时出错了：{}".format(e))
        else:
            print("不支持该种方式")
            resp = None
        return resp
if __name__ == '__main__':
    method = 'post'
    headers={'token':'923FC0CFF48A067CCC2C034714D8D321'}
    #token='FE722A89B70529468B9AF1388DA681C6'
    url = 'https://pg-bate.cailian.net/api/sysfunction/functionChildList'
    param = {'id': '1121594'}
    #res = requests.post(url,param,headers=headers,verify=False)
    res = HttpRequests().http_request(method,url,param,headers,verify=False)
    print(res.json())


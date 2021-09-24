# web自动化测试 Selenium

# Selenium 的原理：必问
# HTTP 协议搭建的 webdriver 接口。
# 1. service 服务 ==》 subprocess ==> 自动的运行 chromedriver.exe
# chromdriver 再对应的端口开一个 webdriver 服务。 9515
# 2.ChromeRemoteConnection  ==> 类似于 requests urlib3 ==> requests.post(host:9515/接口地址，json={})
import requests
from selenium import webdriver

driver = webdriver.Chrome(port=9515)

# 访问百度页面

# api
# driver.get('http://www.baidu.com')
sessionid = driver.session_id
# webdriver 的接口地址，requests ,接口地址。commands = []

url = 'http://localhost:9515/session/{}/url'.format(sessionid)

baidu_url = 'http://www.baidu.com'
data = {'url': baidu_url}
requests.post(url, json=data)

# 获取元素 接口文档没有，不知道参数需要传递什么。
url = 'http://localhost:9515/session/{}/element'.format(sessionid)

# driver.find_element()
data = {'using': "css selector",'value': "#kw"}

res = requests.post(url, json=data).text

print(res)

# 笔试题和面试题
# 简历怎么写。如果没有接到面试电话，简历。
# 又面试却通不过。技术复习，口头表达能力。


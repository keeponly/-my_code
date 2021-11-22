# python == webdriver（接口） == 浏览器

# python 处理接口 == 》 接口自动化测试的时候 ==》 requests

# 我要定位 baidu.com 首页 一个 id = kw 的元素
import requests


def get(webdriver_url, site_url):
    """访问url.访问webdriver. 通过参数传递目标网站的地址"""
    requests.get(webdriver_url, params={"url":site_url})
    return


def get_element_by_id(id):
    """查找对应的id的元素"""
    # 访问查找元素的 webdrier的地址
    # 2. 通过参数传递对应的 id
    # webdriver 告诉浏览器，你去查找这个id
    pass


from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"d:\chromedriver.exe",
                          port=4000)

session = driver.session_id
print(session)
data = {"url":"http://www.baidu.com"}
res = requests.post("http://localhost:9515/session/{}/url".format(session), data)
# url = 'http://www.baidu.com'
# driver.get(url)


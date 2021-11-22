# _*_coding: utf-8 _*_
# @Time     :2019/6/20  9:47
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :learn_wait.py  
# @Software :PyCharm
import time
from selenium.webdriver import Chrome
driver = Chrome()
url = "http://www.baidu.com"
driver.get(url)
time.sleep(3)  # 等待三秒
driver.get('http://www.douban.com')
print(driver.title)  # 获取网络标题
print(driver.current_url)  # 获取网络地址
driver.get_screenshot_as_png('test.png')  # 截屏
print(driver.current_window_handle)  # 获当前窗口id
print(driver.window_handles)   # 获所有窗口id
# driver.maximize_window()  # 最大化游览器
# driver.minimize_window()  # 最小话游览器
# driver.refresh()  # 刷新按钮
# driver.back()  # 后退
# driver.forward()  # 前进
# driver.close()  # 关闭标签,当只有一个标签打开时,等于关闭游览器
# 获取元素属性
# ele_name = ele.get_attribute("name")
# 修改元素属性
# print(ele)
# print(type(ele_name))
driver.quit()  # 关闭游览器

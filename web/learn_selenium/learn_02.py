# _*_coding: utf-8 _*_
# @Time     :2019/6/21  11:04
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :learn_02.py  
# @Software :PyCharm
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver = Chrome()
URL = "file:E:\新建文件夹\web\leran_html\learn_js.html"
driver.get(URL)
driver.find_element_by_name("click").click()
alert = driver.switch_to.alert # 获取弹窗
alert.text  # 查看弹框文本
print(alert.text)
time.sleep(3)  # 等待三秒
alert.accept()  # 确认
# alert.dismiss()  # 取消
# driver.add_cookie()
driver.get_cookie()
driver.quit()
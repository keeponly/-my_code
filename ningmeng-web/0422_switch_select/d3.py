# alert 切换


import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Chrome()
driver.implicitly_wait(20)

driver.get('file:///D:/data/%E7%8F%AD%E7%BA%A7/python14/0422_ui2/index.html')

driver.find_element_by_name('click').click()

# 接受 Alert 对象
alert = driver.switch_to.alert

# # 获取文本内瓤
alert.text

# 确认。返回原来的页面
alert.accept()
# 取消。  返回原来的页面
alert.dismiss()

# 扩展知识 @propty

# 添加 cookie
driver.add_cookie({'name':"yuze"})

# 获取
driver.get_cookie('name')

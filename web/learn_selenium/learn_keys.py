# _*_coding: utf-8 _*_
# @Time     :2019/7/1  11:32
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :learn_keys.py  
# @Software :PyCharm  
"""模拟键盘输入"""

from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome

driver = Chrome()
url = "http://www.baidu.com"
driver.get(url)
ele = driver.find_element_by_id("kw")
ele.send_keys('adminll', Keys.BACKSPACE, Keys.BACKSPACE)
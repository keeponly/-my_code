# _*_coding: utf-8 _*_
# @Time     :2019/7/1  11:59
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :learn_js.py  
# @Software :PyCharm
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
"""鼠标操作"""
driver = Chrome()
driver.implicitly_wait(20)  # 隐式等待
URL = "https://www.12306.cn/index/"
driver.get(URL)


def wait_find_ele(locator) -> WebElement:
    wait = WebDriverWait(driver, timeout=30, poll_frequency=0.1)
    input_ele = wait.until(ec.presence_of_element_located(locator))
    return input_ele
"""python 如何间接修改html属性,只能传输js代码"""
"""ele = driver.find_element_by_id("kw")
 print(ele.get_attribute('class')) 获得元素属性"""

data_ele = wait_find_ele((By.ID, "train_date"))

js_code = 'arguments[0].read0nly=false'
driver.execute_script(js_code, data_ele)

driver.execute_script(js_code, data_ele)
js_code1 = 'arguments[0].value = "2019-08-01"'
driver.execute_script(js_code1, data_ele)

# 修改readonly属性,修改value值,为2019-08-01
# js_code = "e = document.getElementById('train_date');"
# driver.execute_script(js_code) #  在当前窗口执行js命令
# time.sleep(5)
# js_code1 = "e.readOnly = false;"
# driver.execute_script(js_code1)
# time.sleep(5)
# js_code2 = "e.value = '2019-08-01'"
# driver.execute_script(js_code2)
# time.sleep(5)
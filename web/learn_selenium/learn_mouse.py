# _*_coding: utf-8 _*_
# @Time     :2019/6/24  23:31
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :learn_mouse.py  
# @Software :PyCharm
"""鼠标悬停"""
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
URL = "HTTP://www.baidu.com"
driver.get(URL)


def wait_find_ele(locator) -> WebElement:
    wait = WebDriverWait(driver, timeout=30, poll_frequency=0.1)
    input_ele = wait.until(ec.presence_of_element_located(locator))
    return input_ele


ele = wait_find_ele((By.XPATH, "//span[@name = 'tj_settingicon']"))  # 定位设置
set_baidu = wait_find_ele((By.XPATH, "//a[@target = '_blank' and contains(@href, 'gaoji')]"))
# 定义一个动作链条,鼠标动作
ac = ActionChains(driver)
time.sleep(5)
#  将鼠标移动到元素ele上面
wd = ac.move_to_element(ele).perform()
ac.click(set_baidu).perform()
# .click(set_baidu)  # 鼠标悬停
# ac.click()  # 点击
# ac.context_click()  # 右击
ac.drag_and_drop()
# ac.perform()  # 结束

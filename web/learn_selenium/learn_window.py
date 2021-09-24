# _*_coding: utf-8 _*_
# @Time     :2019/6/24  21:22
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :learn_window.py  
# @Software :PyCharm  
import time

from selenium.webdriver.support.select import Select
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = Chrome()
driver.implicitly_wait(20)  # 隐式等待
URL = "HTTP://www.baidu.com"
driver.get(URL)
# 显式等待,初始化计时器,30秒,0.1秒查找一次


def wait_find_ele(locator) -> WebElement:
    wait = WebDriverWait(driver, timeout=30, poll_frequency=0.1)
    input_ele = wait.until(ec.presence_of_element_located(locator))
    return input_ele


ele = wait_find_ele((By.XPATH, "//a[@name = 'tj_settingicon' and contains(@href,'http')]"))
ele.click()
set_baidu = wait_find_ele((By.XPATH, "//a[@target = '_blank' and contains(@href, 'gaoji')]")).click()
select = wait_find_ele((By.XPATH, "//select[@name = 'ft']"))
"""获取select里面的选项"""
sel_new = Select(select)
time.sleep(5)
sel_new.select_by_value("pdf")

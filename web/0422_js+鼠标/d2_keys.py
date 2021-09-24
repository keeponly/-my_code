"""
链式调用。 actionChains

1. 每次都是return self
2. perform(),  run()

作用：用在连续调用，一次运行不同的程序或者函数。
：数据库。ORM 模型。 ==> 链式调用。


函数：
1. click()
2. double——click()
3. context_click()
4. click_and_hold()
4. drag_and_drop()
move_to_element
move_to_element


# 输入键盘
"""
import time

from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Chrome()
driver.implicitly_wait(20)

def wait_find_element(locator) -> WebElement:
    wait = WebDriverWait(driver, timeout=30, poll_frequency=0.5)
    input_ele = wait.until(EC.presence_of_element_located(locator))
    return input_ele

driver.get('http://www.baidu.com')
from selenium.webdriver.common.keys import Keys


"""keys 键盘位置。
ctrl
enter


"""
ele = driver.find_element_by_id('kw')
ele.send_keys('admin', )

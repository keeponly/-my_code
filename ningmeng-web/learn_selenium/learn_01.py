# _*_coding: utf-8 _*_
# @Time     :2019/6/20  10:52
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :learn_01.py  
# @Software :PyCharm  
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver = Chrome()
URL = "http://www.baidu.com"
driver.get(URL)
# 显式等待,初始化计时器,30秒,0.1秒查找一次


def wait_find_ele(locator) -> WebElement:
    wait = WebDriverWait(driver, timeout=30, poll_frequency=0.1)
    input_ele = wait.until(ec.presence_of_element_located(locator))
    return input_ele


# 窗口切换
current_handls = driver.window_handles
wait = WebDriverWait(driver, timeout=30, poll_frequency=0.1)
wait.until(ec.new_window_is_opened(current_handls))

"""
iframe切换
# frame = driver.find_element_by_tag_name("iframe")
# driver.switch_to.frame(frame)
ec.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframename")) 等待
driver.switch_to.default_content() 切换回原页面
driver.switch_to.parent_frame() 多层iframe嵌套,切换回上一层iframe
"""

ele = wait_find_ele((By.ID, "kw")).send_keys("柠檬班")
sub_element = wait_find_ele((By.ID, "su")).click()
ningmeng = wait_find_ele((By.XPATH, "//a[contains(text(),'lemon.ke.qq.com/')]")).click()
img = wait_find_ele((By.TAG_NAME, 'img'))
print(img)
driver.quit()
# 前程贷地址：http://120.78.128.25:8765
# 账号：18684720553
# 密码：python
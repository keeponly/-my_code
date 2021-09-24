"""
1. 鼠标操作 ActionChains 链式调用，存储动作。 函数的动态调用

1. 单击 click(element) ==> 移动到对应的元素，再点击 ,driver.click()
2. 双击
3. 右击 context_click
4. 鼠标悬停  move_to_element
5. 拖拽， drag_and_drop

perform()

超市：1.满50 - 9 2. 8折。  3. 5优惠。 开发思维， 数据ORM

2. Key, 键盘发送  send_key()
3. JS 脚本发送。 作用：因为python 操作浏览器，有的东西操作不了，没有办法直接操作。
js

1. 原生的 js 脚本 2. 先通过 selenium 找到对应的元素。 arguments[0]
driver.execute_script(js_code)

js = "arguments[0].value='new_value'"
driver.execute_script(js, element)


文件发送。面试题。

"""
import time
#
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#
driver = Chrome()
driver.implicitly_wait(20)
#
def wait_find_element(locator) -> WebElement:
    wait = WebDriverWait(driver, timeout=30, poll_frequency=0.5)
    input_ele = wait.until(EC.presence_of_element_located(locator))
    return input_ele
#
# def wait_clickable_element(locator) -> WebElement:
#     wait = WebDriverWait(driver, timeout=30, poll_frequency=0.5)
#     input_ele = wait.until(EC.element_to_be_clickable(locator))
#     return input_ele
#
driver.get('file:///D:/data/%E7%8F%AD%E7%BA%A7/python14/0422_%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0/index.html')
#
# 定位文件发送的元素
e = driver.find_element_by_name('myfile')
e.send_keys(r'D:\test.xlsx')

# 文件发送有时候他并不是通过 input type=file 的形式来进行传递的。


#



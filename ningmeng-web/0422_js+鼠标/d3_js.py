"""
js 脚本

python - webdriver -  JS 桥梁  - 浏览器


1 . find_element_by_id(id)  ==> {"by":"id", "value": "kw" } js:  命令：getElemenetById(id)

2. python 发送 js 代码  ==>  {"by":"script", "value": "document.getElementById('kw')"}
"""

# js 脚本运行。
# python 怎么修改属性？ python 能直接修改 hTML 属性吗？
# python 是不能直接修改 HTML 属性

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
# driver.get('http://www.baidu.com')
#
# ele = driver.find_element_by_id('kw')
# ele.get_attribute('name')  # wd
# ele.set_attrit   js， webdriver.


# 没有现成的命令（方法）去修改 HTML, 只能传输 js 代码给js 去运行
# value,  set_attribute('value', new_value)
# setAttribute(),  ele.value =   ele.readOnly = false;


# 访问 12306
driver.get('https://www.12306.cn/index/')

# date_ele = wait_find_element((By.ID, 'train_date'))
# print(date_ele)

# 修改 readOnly,  把 value = 2019-04-26
# TODO:一定要记得休眠哦。
# js_code = "e = document.getElementById('train_date');"
# ele = driver.execute_script(js_code)
# time.sleep(2)
# js_code1 = "e.readOnly = false;"
# driver.execute_script(js_code1)
# time.sleep(2)
# js_code2 = "e.value = '2019-05-26'"
# driver.execute_script(js_code2)
# time.sleep(2)



date_ele = wait_find_element((By.ID, 'train_date'))
print(date_ele)

js_code = 'arguments[0].readOnly=false'
driver.execute_script(js_code, date_ele)

# python
print("欢迎来到柠檬班 {0} 次 {1}".format(1,3))

js_code1 = 'arguments[0].value="2019-05-26"'
driver.execute_script(js_code1, date_ele)






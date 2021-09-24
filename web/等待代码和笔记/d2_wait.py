import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = Chrome()

# 隐式等待。
driver.implicitly_wait(30)

driver.get('http://www.baidu.com')

# 页面生命周期  预加载 + 加载控件，内容，图片，文件。 + 卸载
# 后期加载，AJAX

# 等待

# 显示等待

# 初始化计时器
wait = WebDriverWait(driver, timeout=30)
# if
ele = wait.until(ec.presence_of_element_located((By.XPATH, '//input[@id="kw"]')))

# ele = driver.find_element_by_id('kw')


# 动态等待的思路
# continued = True
# timeout = 10
# while continued:
#     try:
#         ele = driver.find_element_by_id('kw')
#         continued = False
#     except Exception as e:
#         continue


# 获取属性
ele_name = ele.get_attribute('name')
print(ele)
print(type(ele_name))
# 修改元素属性, 为啥python selenium 没有 set_attribute方法。
# 无法直接通过 python 执行修改动作。
# python == webdriver ==( JS==浏览器 )

# 输入文本内容
ele.send_keys('柠檬班')

# 提交

submit_ele = driver.find_element_by_id('su')
submit_ele.click()

time.sleep(3)

# 如果页面正在加载中，你却在执行 find_element()
# 当找元素的时候，你发现报错了，No Such Element, Element can not located.
# 1. 元素表达式有问题， 2. 你没有等待。 3. 元素不可用，（隐藏，不能用）
# 1. 元素表达式有问题， 2. 你没有等待。 3. 元素不可用，（隐藏，不能用）



# 3 种等待：1. 强制的，2. 隐式， 3. 显性等待
# find_element 强制等待（休息，睡觉）
# 张学友演唱会。 摄像头，监控 隐式等待==》
# 特别行动小组。门口，门卡


# 显示等待。

driver.quit()


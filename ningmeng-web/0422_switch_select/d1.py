"""
等待：
1. 强制等待：想要指定的等待时间；
2. 隐式等待：监控。浏览器会话只需要使用一次。
3. 显式等待：
"""
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Chrome()
driver.implicitly_wait(20)

driver.get('http://www.baidu.com')

# 计时器：1. 第一个参数
# wait = WebDriverWait(driver, timeout=30, poll_frequency=0.5)
# wait.until(EC.presence_of_element_located((By.ID, 'kw')))


# 定位柠檬班的图片

# 定位 input 输入框

# 函数注解
def wait_find_element(locator) -> WebElement:
    wait = WebDriverWait(driver, timeout=30, poll_frequency=0.5)
    input_ele = wait.until(EC.presence_of_element_located(locator))
    return input_ele


# driver.find_element_by_id('kw')
input_ele = wait_find_element((By.ID, 'kw'))
input_ele.send_keys('柠檬班')

# input_ele.send_keys('柠檬班')
# 定位百度一下

# sub_ele = wait_find_element((By.ID, 'su'))
# sub_ele.click()

# 快捷方式，当输入的内容再一个 form 表单里面的时候，可以使用 ele.submit() 来进行提交
input_ele.submit()



# 定位柠檬班腾讯课堂
nm_ke = wait_find_element((By.XPATH, "//a[contains(text(), 'lemon.ke.qq.com/')]"))

nm_ke.click()

time.sleep(2)
#窗口切换，首先要获取到每一个窗口的 id,
# 窗口的句柄或者窗口的名字


# 窗口切换的等待
# EC.wind
current_handles = driver.window_handles
wait = WebDriverWait(driver, timeout=30, poll_frequency=0.5)
wait.until(EC.new_window_is_opened(current_handles))


# iframe 切换


# print(driver.window_handles)
# driver.switch_to.window(driver.window_handles[1])

#
# # 点击定位图片
# img = wait_find_element((By.TAG_NAME, 'img'))
# print(img)




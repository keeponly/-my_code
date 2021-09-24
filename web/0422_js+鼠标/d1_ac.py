"""文件上传


三大切换
Select
cookie

窗口切换

self.current_handles(参数，函数)某一个时刻打印 driver.window_handles  != driver.current_handle


iframe, ==> 怎么切换主页面， switch_to.default_content()
==> 上一级iframe   switch_to.parent_frame()


alert

鼠标操作
1. 最简单的鼠标操作。 点击， click()
2. 右击。
3. 双击。
4. 鼠标悬停




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

def wait_clickable_element(locator) -> WebElement:
    wait = WebDriverWait(driver, timeout=30, poll_frequency=0.5)
    input_ele = wait.until(EC.element_to_be_clickable(locator))
    return input_ele

driver.get('http://www.baidu.com')

# ele = driver.find_element_by_id('kw')
# res = ele.click()
# # 没有返回值
# print(res)
#
# # ActionChains  动作链条
# ac = ActionChains(driver)
# # 第一不：鼠标悬停
# ac.move_to_element()
# # 第二部：点击动作
# ac.click()
# # 第三步：右击
# ac.context_click()
# # 以 perform 结束
# ac.perform()
#
# # 总体去运行
# ac = ActionChains(driver)
# ac.move_to_element().context_click().perform()

# 举例子用   到高级搜索
# ActionChains  动作链条
ac = ActionChains(driver)
ele = wait_clickable_element((By.XPATH, "//a[text()='设置' and contains(@href, 'http')]"))
gj = wait_find_element((By.XPATH, "//a[text()='高级搜索']"))

ac.move_to_element(ele).click(gj).perform()

# gj =
ac.move_to_element(ele).perform()

ac.click(wait_find_element((By.XPATH, "//a[text()='高级搜索']"))).perform()

# .click(wait_find_element((By.XPATH, "//a[text()='高级搜索']")))

time.sleep(2)





import time

from selenium.webdriver import Chrome
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

# 定位设置 tj_settingicon  //a[text()='设置' and contains(@href, 'http')]
ele = wait_find_element((By.XPATH, "//a[text()='设置' and contains(@href, 'http')]"))
ele.click()

# 高级搜索
gj = wait_find_element((By.XPATH, "//a[text()='高级搜索']"))
gj.click()

# 定位 select
# select = wait_find_element((By.XPATH, "//select[@name='ft']"))
# select.click()
#
# # 等待省略
# select.find_element_by_xpath('//option[@value="pdf"]').click()
# e.find


# 第二种方法： Select
select = wait_find_element((By.XPATH, "//select[@name='ft']"))
sle_new = Select(select)
# 选项：1.value, 2,indix, 3.text
sle_new.select_by_value('pdf')
# 取消选择,意义对应 + all
sle_new.deselect_all()


# 三大切换
# window 切换: 1. 拿到 window 的句柄，
# name 2. print(window_handlers, current_windwow_handle)

# 窗口等待， EC.new_window_is_opened(current_handlers)

# iframe: 1. frame() 3:索引 2. name 3. WebElement
# 等待： frame_to_be_available_and_switch_to_it()
# EC.frame_to_be_available_and_switch_to_it

# 弹窗切换: alert. Alert类：text, accept(), dismiss()

# Select: 告诉了我们：如果你觉得 click 不好用， 你自己封装。

# find_element() 不仅可以再 driver 对象上用，还可以再 WebElement 对象用 ==》 下属标签里面去查找。

# 函数注解 -> list:

# 添加 cookie
driver.add_cookie({'name':"yuze"})

# 获取
driver.get_cookie('name')

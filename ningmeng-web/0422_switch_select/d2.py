"""
iframe 切换
1. name
2. 索引
3. WebElement
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

driver.get('file:///D:/data/%E7%8F%AD%E7%BA%A7/python14/0422_ui2/index.html')


driver.switch_to.frame('myiframe')
# 先要拿到 WebElement
# frame = driver.find_element_by_tag_name('iframe')
# driver.switch_to.frame(frame)

# 等待新的iframe 可以用再进行切换。
EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, 'iframe'))

# 怎么切回初始的 HTML 内容
driver.switch_to.default_content()

# iframe 多层嵌套, 切到父级iframe
driver.switch_to.parent_frame()




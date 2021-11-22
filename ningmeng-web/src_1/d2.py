# selenium 使用元素定位
import requests
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

# 1. 通过id查找
ele = driver.find_element_by_id('ksfjoo')
print(ele)

# 2. 通过class
ele = driver.find_element_by_class_name("s_ipt")
print(ele)

eles = driver.find_elements_by_class_name("s_ipt")
print(eles)
# 1. 个是 webElement, 列表
# 2. find_element 找到的是第一个

# 3  name  江湖名字==》响亮==》极有可能是唯一的。
eles = driver.find_element_by_name('wd')

# 4. tagname 太不唯一
eles = driver.find_element_by_tag_name('input')
# 5. link_text
ele = driver.find_element_by_link_text('新闻')
#6. partial_link_text 包含
ele = driver.find_element_by_partial_link_text('新')
# css选择器
ele = driver.find_element_by_css_selector("input#kw")
# xpath ==> css选择器的作用

requests.get()

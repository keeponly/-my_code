# _*_coding: utf-8 _*_
# @Time     :2019/6/17  16:18
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :learn_selenium.py  
# @Software :PyCharm  
import requests
from selenium import webdriver
#
#
# def get(webdriver_url, site_url):
#     requests.get(webdriver_url, params={"url": site_url})
#
#
# def get_element_by_id(id):
#     pass

driver = webdriver.Chrome()
url = "http://www.baidu.com"
driver.get(url)
# 唯一input
ele = driver.find_element_by_id("kw")
# 江湖名称,经常使用,很有可能唯一
ele = driver.find_element_by_name("wd")
ele = driver.find_element_by_tag_name("input")
# 文本超链接
ele = driver.find_element_by_link_text()
ele = driver.find_element_by_partial_link_text()
# css选择器  # 代表id ,.代表class
ele = driver.find_element_by_css_selector("input#kw")

"""
xpatn定位
//表示父子关系,祖先关系
/表示父子关系
@表示属性
//span/input[@id='kw' and @name='wd']
//*/input[@id='kw' and @name='wd']
//*/input[@*='kw']
//a[text()="新闻"]
//a[contains(text(),"地")] 包含,元素属性里面包含某个字符
//input[@id="kw"]/..  层级关系,返回上一级
"""


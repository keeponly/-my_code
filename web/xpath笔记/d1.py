"""
复习：
selenium
"""

from selenium import webdriver


driver = webdriver.Chrome()
# driver.session_id
# 卸载selenium  pip uninstall selenium
# 使用 requests 去访问 selenium webdriver 暴露的接口地址。 session_id.

# 怎么进行元素定位， id, name, class_name, tag_name,
# link_text, partial_link_text, css_selector, Xpath

# id, name, class_name, tag_name ==> find_element() ==> 转成 css 选择器
# ==》 find_element_by_css_selector()

# Xpath, 自动化测试人员的绝世秘籍， Xpath, 天下没有我找不到的元素。

# python， JS, HTML标记型语言，CSS,美化， xpath,专门用来表示路径的语言。

# TODO: 能用相对路径，就不要用绝对路径。
# 1. 相对路径更加稳定，可读性也更强。

# css 和 xpath 缩小范围，更加精确。
# 元素的组成：tagname 属性， text, 下属标签 ==》DOM
# 但斜杠，只能表示父子，//既可以表示父子，也可以表示隔代关系，个很多代的关系
# 【】 表示 谓语条件
# * 号表示任意的
# 层级关系 .当前层级 /..上一级
# 轴运算

# ipt < s_ipt    fsowoef < s_ipt wofos fsowoef woofof

# TODO:面试题：css 选择器 和 xpath 区别：优劣是什么？什么时候使用
# 1。更加简洁
# 2. chrome, firefox 速度快一些，效率高一些。 xpath 在IE浏览快

# 1. text
# 2. 复杂的元素查找时，xpath 反而更加简单。 xpath 功能更加强悍。

# 当你要找的元素表达式比较简单，css, 复杂的时候用 xpath

driver.get('http://www.baidu.com')

ele = driver.find_element_by_xpath("//input[@id='kw']")

print(ele)


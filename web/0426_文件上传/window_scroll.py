"""窗口拖动，滚动

原因：是因为特定的时候，只有讲窗口滚动到合适的位置，某个元素才能被使用。

js_code.
"""

# 发送窗口拖动的 js 脚本
# js_code = "window.scrollTo(0, document.body.scrollHeight)"
# driver.execute_script(js_code)


# 第二种 selenium

from selenium.webdriver import Chrome

driver = Chrome()
driver.get("file:///D:/data/%E7%8F%AD%E7%BA%A7/python14/0422_%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0/index.html")

# 定位元素
e = driver.find_element_by_name('myfile')

e.location_once_scrolled_into_view()


# 富文本域 textarea
# 不能使用 send_keys


# js 的形式，修改里面的 innerHTML

# 定位无敌 xpath

# 操作
# js 脚本 ==> 葵花宝典。
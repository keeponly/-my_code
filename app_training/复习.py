"""
混合应用：1、切换。 相当于 web iframe
不同的页面，==》 不同的环境 ==》 上下文
driver.switch_to.context()

# 切换上下文，写框架。basepage switch_context()

# 怎么辨别一个网页：
- viewer 1、图形，一整块、对 2、xml 属性，class, webview

3、浏览器版本和chromedriver 要匹配

# appium app, 成熟方案，稳定性不高。 web 自动化
# 跨平台，切换
# uiautomator, python, pyuiautomator

subprocess.

# 1、好不好用：灵活性、可读性、扩展性。
# BasePage, PO, DDT, locator, 数据管理分组、前置条件。分层。
# app, 添加新东西，修改原来 web 的部分代码。


app web 有什么区别：
实战项目和 web :
# 细节不同
# 流程一样的。
1、basepage, app 相关的很多其他操作， swipe, 电源，back
2、PO， 设计不太一样。页面更加模糊
3、数据分组，
error = [

"""
error = [
    {"phone":"", "pwd":"", "expect":"错误"},
    {"phone":"", "pwd":"", "expect":"错误"},
]


error_phone = [
    {"phone":"", "expect":"错误"},
    {"phone":"", "expect":"错误"},
]


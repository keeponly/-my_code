from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:
    """登录页面。 PageObject。"""


    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://120.78.128.25:8765/Index/login.html'


    def login(self, username, pwd):
        """登录"""
        # 1. 打开浏览器 open_browser
        # driver = Chrome()

        # 2. 访问登录页面  visit_login_page
        self.driver.get(self.url)

        # 3. 定位元素 find_element 用户如输入框， 密码输入框
        user_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.NAME, 'phone')))
        pwd_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//input[@name='password']")))

        # 4. 发送用户名密码，提交  submit
        user_ele.send_keys(username)
        pwd_ele.send_keys(pwd)
        user_ele.submit()
        return self.driver



    # TODO: 遇到的问题：我们在不同的函数之间要共享某一些变量，很多很多的变量。
    #

    # 函数内部修改全局变量。global
    # PO, 雏形：类属性，实例属性。

    # def logout(self, user, pwd):
    #     driver = Chrome()
    #     driver.get('http://120.78.128.25:8765/Index/login.html')


    # def select_bid(self):
    #     """投资
    #     1. 一个类只做一件事。
    #     2. 不容易维护；
    #     3. 更新的时候会容易造成整个类的破坏
    #     """
    #     pass

    # PageObject  ==> 页面里面的操作和数据  映射成一个 python 类 对象。
    # HTML 页面  ==> DOM  ==> PO
    # PO 思想，类封装。
    # PO 模式：当你要测试的功能和需要调用的函数或者数据越来越多的时候。 维护，更新，方便快捷；
    # 随便堆砌 方法和类：小项目，当你需要调用的函数或者数据比较小的。


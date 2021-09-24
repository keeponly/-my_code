"""测试登录功能  正确的用户名：18684720553"""
import time
import unittest
from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



# 1. 测试，预期结果和实际结果
# 2. 投资，登录
# Selenium 初始化的时候 Option, --headless

from pages.login import LoginPage


class TestLogin(unittest.TestCase):

    def setUp(self):
        # 浏览器初始化
        self.driver = Chrome()
        # 初始化登录页面
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_success(self):
        # 登录
        driver = self.login_page.login('18684720553', 'python')
        # 5. 断言 首页的元素
        # user_ele = driver.find_element_by_xpath("//a[@href='/Member/index.html']")
        user_ele = WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//a[@href='/Member/index.html']")))

        self.assertTrue("小蜜蜂96027921" in user_ele.text)

        time.sleep(2)
        driver.quit()

    # 手机号为空： 请输入手机号码
    # 手机号格式不正确 ： 请输入正确的手机号码
    #     # 密码为空： 请输入密码
    # 密码不正确：弹框：此账号没有经过授权，请联系管理员!

    # 20 组数据， 20 个测试用例的方法吗？ pass

    # def test_login_error_one(self):
    #     # 错误信息定位 div.form-error-info
    #     driver = self.login_page.login('', '')
    #
    #     # e = find_error_element(div.form-error-info)
    #
    #     # 5. 断言 首页的元素
    #     self.assertTrue(e.text, '请输入手机号码')

    # 预期结果，测试数据，用例设计存储到哪里？
    # 真的需要设计 4 个不同的方法吗？
    # ddt, web测试里面如何去实现ddt,  进一步的分层设计，
    #
    # def test_login_error_twow\(self):
    #     driver = login("", 'python')


    # pypiwin32 3.4 不支持
    # pywin32.exe ,安装到 windows, pywin32


if __name__ == '__main__':
    unittest.main()


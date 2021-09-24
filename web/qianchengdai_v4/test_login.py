"""测试登录功能  正确的用户名：18684720553"""
import time
import unittest

import ddt
import pytest
from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



# 1. 测试，预期结果和实际结果
# 2. 投资，登录
# Selenium 初始化的时候 Option, --headless
from pages.index import IndexPage
from pages.login import LoginPage
from test_data.login import user_info_error


# def init_web():
#     """初始化浏览器"""
#     driver = Chrome()
#     login_page = LoginPage(driver)
#     return driver, login_page
#
#
# def finish_web():
#     """退出浏览器"""
#     init_web()
#     driver.quit()





# @ddt.ddt
@pytest.mark.login
@pytest.mark.c
@pytest.mark.test


class TestLogin():

    # def __init__(self):
    #     pass

    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("test begin")
    #     cls.driver = Chrome()
    #     cls.login_page = LoginPage(cls.driver)
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print("test end")
    #     cls.driver.quit()
    #
    # def setUp(self):
    #     # 浏览器初始化
    #     print("test case begin")
    #     # self.driver = Chrome()
    #     # 初始化登录页面
    #
    # def tearDown(self):
    #     print("test case end")
        # clear_user_info()

    @pytest.mark.success
    def test_login_2_success(self):
        # 登录 login
        self.driver = Chrome()
        self.login_page = LoginPage(self.driver)
        self.login_page.login('18684720553', 'python')
        # 5. 断言 首页的元素

        # 获取用户信息 get_user_info()
        # user_ele = driver.find_element_by_xpath("//a[@href='/Member/index.html']")

        user_ele = IndexPage(self.driver).get_user_info()

        # self.assertTrue()
        assert("小蜜蜂96027921" in user_ele.text)

        time.sleep(2)
        self.driver.quit()

    @pytest.mark.demo
    # @pytest.mark.skip(reason="test")
    # @ddt.data(*user_info_error) # (a, b, c)
    @pytest.mark.parametrize('data', user_info_error)
    def test_login_1_error(self, data, init_web, session_web):
        """请输入手机号"""
        # 登录
        # self.driver = Chrome()
        # self.login_page = LoginPage(self.driver)

        self.driver, self.login_page = init_web # 元组

        # self.login_page.login('18684720553', 'python')
        self.login_page.login(data['username'], data['pwd'])
        # 定位出错的信息的元素 get_flash_info()

        # 清空用户数据clear_user_info() 侵犯攻击性

        flash_ele = self.login_page.get_flash_info()
        # 断言
        self.assertTrue(data['expected'] == flash_ele.text)


        # 关键点：数据不同
        # assert (True)
        # 测试用例数据：1. Excel, 2:列表
        # http_request(url, data, method)
        # 数据 == 》 测试， page 页面
        # self.assert
    # def test_login_2_unauth(self, data):
    #     pass
# def test_B():
#     print("hello")
if __name__ == '__main__':
    unittest.main()

    # 随机测试
    # 测试用例发现 add 自动发现
    # 测试环境 fixture
    # 测试报告，pip install pytest-allure
    # 重运行机制




from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.base import BasePage


class LoginPage(BasePage):
    """登录页面。 PageObject。"""
    username_locator = (By.NAME, 'phone')
    pwd_locator = (By.XPATH, "//input[@name='password']")
    url = 'http://120.78.128.25:8765/Index/login.html'


    # def __init__(self, driver):
    #     self.driver = driver
    #     self.url = 'http://120.78.128.25:8765/Index/login.html'

    def login(self, username, pwd):
        """登录"""
        # 1. 打开浏览器 open_browser
        # driver = Chrome()

        # 2. 访问登录页面  visit_login_page
        self.driver.get(self.url)

        # 3. 定位元素 find_element 用户如输入框， 密码输入框 get_username()
        user_ele = self.get_user_info()
        pwd_ele = self.get_pwd_info()

        # 4. 发送用户名密码，提交  submit
        user_ele.send_keys(username)
        pwd_ele.send_keys(pwd)
        user_ele.submit()

        return self.driver

    def get_flash_info(self):
        """获取错误信息"""
        # self.wait_presence_element()
        flash_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, '.form-error-info')))
        return flash_ele

    def clear_user_info(self):
        """清空用户数据"""
        self.clear_username()
        self.clear_pwd()

    def clear_username(self):
        """清空用户"""
        # 定位用户  get_username()
        return self.get_user_info().clear()

    def clear_pwd(self):
        """清空密码"""
        return self.get_pwd_info().clear()

    def get_user_info(self):
        """定位用户名"""
        user_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(self.username_locator))
        return user_ele

    def get_pwd_info(self):
        """定位密码输入"""
        user_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(self.pwd_locator))
        return user_ele




    ## 为什么要多封装怎么多方法
    # 1. 当项目越来越大的时候，只需要使用这些函数，不需要复制具体的代码了。
    # 2. 增加可读性，
    # 3. 中级的要求。10来行， 函数的颗粒度


    # 进一步封装 Locator,元素定位表达式
    # 第一种方式：类属性封装
    # 第二种方式：新建一个 locator 文件夹 。login.py. 优势：发生了变化。劣势：


    # 封层总结：
    # 1. 函数。
    # 2. PageObject, 函数要共享变量
    # 3. DDT 数据分层。 1. 提高复用性；2. 更加容易维护； 3. 可读性更高。
    # 数据分组：1.依据，测试步骤，登录失败，flash_msg, 未授权，alert
    # @ddt.ddt 类  @ddt.data
    # 4. locator 元素定位分层.
    # 5. basepage

    # 提高效率， @classmethod setUpClass(cls):  测试用例：if,定位不成功：换一种方式。






from pages.login import LoginPage
from pages.nav import NavPage
from pages.user import UserPage


def test_login_success(init_app_reset):
    """测试登录成功"""
    # 初始化 fixture 环境 conftest.py
    driver = init_app_reset
    # 滑屏进入首页
    # 导航我的
    # 前置条件：未登录。重置应用。noReset= false
    NavPage(driver).user()
    # 登录
    LoginPage(driver).login('18684720553','python')
    # 输入用户名

    # 输入密码

# def test_login_success(init_app_noreset):
#     """测试登录成功"""
#     # 初始化
#     driver = init_app_noreset
#     # 导航我的
#     NavPage(driver).user()
#     # 登录
#     LoginPage(driver).login('18684720553','python')


# 相关性。用户  ==> 功能
# 投资。用户    ==>
# 首页。
# 设置。
# class==>种类，差不多，关联 Dog:


# 实体页面：web
# 如果一个页面里面涉及的操作比较多。你可以单独做成一个页面
# 如果页面功能单一，手机号码，密码页面。注册/登录 regester_or_login, 用户 user
# start_activity
# 业务、用例设计能力。

# class Mobile:
#
#     mobile_locator = (By.ID, "")
#
#     def get_mobile(self):
#         pass
#
#     def click_next(self):
#         pass
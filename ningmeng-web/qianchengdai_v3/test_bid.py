import unittest

from selenium import webdriver

from pages.bid import BidPage
from pages.index import IndexPage
from pages.login import LoginPage
from pages.user import UserPage
from test_data.bid import invest_money
from test_data.login import user_info_success

"""投资的前置条件：
1. 登录
2. 有没有余额 1. 查询余额，充值（） 2. 接口 3. 数据库 4. 100亿，手动充值
全部都自动化测试：手工测试
3. 标有没有钱 手动
"""

class TestBid(unittest.TestCase):

    def setUp(self):
        """登录"""
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)
        self.login_page.login(user_info_success['username'], user_info_success['pwd'])
        self.bid_page = BidPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_bid_success(self):
        # 在首页选择标的 choose_bid() , 点击投标
        IndexPage(self.driver).choose_bid()

        # 定位投资输入框元素 get_bid_input_element()
        e = self.bid_page.get_bid_input_element()

        expect = float(e.get_attribute('data-amount'))
        print(expect)

        # 发送投资金额
        e.send_keys(invest_money)
        # 点击投资
        self.bid_page.click_bid_submit()
        # 激活并查看
        self.bid_page.click_alert()

        actual_money_str = UserPage(self.driver).get_user_money()
        actual_money = float(actual_money_str)

        # 调试步骤
        print(int(expect*100))
        print(int(invest_money*100))
        print(int(actual_money)*100)

        self.assertTrue( int(expect*100) -invest_money*100 == int(actual_money)*100 )



if __name__ == '__main__':
    unittest.main()


    # 冒烟


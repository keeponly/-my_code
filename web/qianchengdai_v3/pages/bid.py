from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.base import BasePage


class BidPage(BasePage):
    """投资页面。 PageObject。"""

    # 投资输入框
    bid_input_locator = (By.XPATH, "//input[contains(@class, 'invest-unit-investinput')]")
    # 按钮的元素定位
    bid_submit_locator = (By.XPATH, "//a[@href='/loan/loan_detail/Id/15119.html' and @class='btn btn-special']')]")
    # 投资激活定位
    alert_active_locator = (By.XPATH, "//div[@class='layui-layer-content']//button[text()='查看并激活']")

    def get_bid_input_element(self):
        """定位投资输入框"""
        return self.wait_presence_element(self.bid_input_locator, timeout=20)

    def click_bid_submit(self):
        """点击投标按钮"""
        e = self.wait_clickable_element(self.bid_submit_locator)
        e.click()

    def click_alert(self):
        """点击激活并查看"""
        e = self.wait_clickable_element(self.alert_active_locator)
        e.click()
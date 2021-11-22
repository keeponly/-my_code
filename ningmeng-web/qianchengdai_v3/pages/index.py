#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:muji
# datetime:2019/5/8 20:11

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.base import BasePage


class IndexPage(BasePage):
    """首页类"""
    bid_locator = (By.XPATH, "//a[contains(@class, 'btn-special')]")

    # def __init__(self, driver):
    #     self.driver = driver

    def get_user_info(self):
        """获取首页的用户信息"""
        user_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//a[@href='http://120.78.128.25:8765/Index/index.html']")))
        return user_ele

    def choose_bid(self):
        """选择标的"""
        # 定位投标这个按钮。
        e = self.wait_clickable_element(self.bid_locator)
        # 点击
        return e.click()

        # 首页  不同类之间共享的特征，继承 basepage
        # 登录页面
        # 投资页面
        #
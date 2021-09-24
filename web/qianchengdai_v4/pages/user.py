#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:muji
# datetime:2019/5/10 21:25

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.base import BasePage


class UserPage(BasePage):
    """用户页面。 PageObject。"""
    user_money_locator = (By.CSS_SELECTOR, ".color_sub")

    def get_user_money(self):
        e = self.wait_presence_element(self.user_money_locator)
        money = e.text[:-1].strip()
        return money  # 字符串


#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:muji
# datetime:2019/5/8 20:11

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class IndexPage:
    """首页类"""

    def __init__(self, driver):
        self.driver = driver


    def get_user_info(self):
        """获取首页的用户信息"""
        user_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//a[@href='/Member/index.html']")))
        return user_ele
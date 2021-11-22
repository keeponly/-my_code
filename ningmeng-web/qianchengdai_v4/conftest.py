#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:muji
# datetime:2019/5/13 21:49
import pytest
from selenium.webdriver import Chrome

from pages.login import LoginPage


@pytest.fixture()
def init_web():
    driver = Chrome()
    login_page = LoginPage(driver)

    yield driver, login_page

    driver.quit()
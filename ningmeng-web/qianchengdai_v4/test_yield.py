#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:muji
# datetime:2019/5/13 21:39
import pytest


@pytest.fixture()
def init_web():
    print("初始化浏览器")

    yield

    print("退出浏览器")


@pytest.fixture(scope='class')
def class_web():
    print("class before")

    yield

    print("class after")

@pytest.fixture(scope='module')
def module_web():
    print("module before")

    yield

    print("module after")


@pytest.fixture(scope='session')
def session_web():
    print("session before")

    yield

    print("session after")


# @pytest.fixture(scope='class')
# def global_web():
#     driver = webdriver.Chrome()
#
#     yield
#
#     driver.quit()

    print("session after")

class TestA:

    @pytest.mark.q
    def test_demo(self, init_web, session_web, class_web, module_web):
        print("执行测试用例。")

    @pytest.mark.q
    def test_1_demo(self, init_web, session_web, class_web, module_web):
        print("执行测试用例2")


class TestB:
    @pytest.mark.q
    def test_3_demo(self, init_web, session_web, class_web, module_web):
        print("执行测试用例3")

# pytest


# init_web 3, session:1,  class:2, module:1

# 重运行 pytest-rerunfailures
# pytest --reruns 5 --reruns-delay 5

# jenkins
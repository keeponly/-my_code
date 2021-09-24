import pytest
import yaml
# pip install py-yaml

from pages.base import BasePage
from pages.guide import GuidePage
from pages.home import HomePage
from pages.nav import NavPage
from setting.config import caps_path
from appium.webdriver import Remote

# caps 配置：1、py文件 2、ini  3、yaml 灵活，不同的语言 .yaml .yml
caps = yaml.load(open(caps_path)) # 字典

# yaml.load


@pytest.fixture
def init_app_reset():
    # caps
    # caps = {'automatorName'}
    driver = Remote(desired_capabilities=caps)
    GuidePage(driver).enter_home()
    yield driver
    driver.quit()


@pytest.fixture
def init_app_noreset():
    # caps
    caps['noReset'] = True
    driver = Remote(desired_capabilities=caps)
    # 如果不在首页，滑屏，如果在首页直接初始化
    try:
        # 在首页？？
        HomePage(driver).get_projects()
    except Exception as e:
        GuidePage(driver).enter_home()

    yield driver

    driver.quit()

def init_app_71_version():
    pass




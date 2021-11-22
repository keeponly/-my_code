from appium.webdriver import Remote

from pages.guide import GuidePage
from pages.login import LoginPage
from pages.nav import NavPage
from pages.user import UserPage

caps = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "Android Emulator",
    "appActivity": "com.lemon.lemonban.activity.MainActivity",
    "appPackage": "com.lemon.lemonban",
    # "noReset": "true",
}

driver = Remote(desired_capabilities=caps)

GuidePage(driver).enter_home()

NavPage(driver).user()

LoginPage(driver).login('18684720553', 'python')

UserPage(driver).create_gesture((1, 5, 7, 9))

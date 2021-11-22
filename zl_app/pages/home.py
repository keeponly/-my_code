from appium.webdriver.common.mobileby import MobileBy as By
from pages.base import BasePage


class HomePage(BasePage):
    login_locator = (By.ID, 'com.xxzb.fenwoo:id/btn_login')
    prjects_locator = (By.ID, 'com.xxzb.fenwoo:id/textView')

    def login_or_register(self):
        return self.click(self.login_locator)

    def get_projects(self):
        return self.get_visible_element(self.prjects_locator)

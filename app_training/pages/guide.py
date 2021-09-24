import time
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base import BasePage


class GuidePage(BasePage):
    pages = 3
    enter_locator = (By.ID, 'com.lemon.lemonban:id/navigation_my')

    def guide(self):
        time.sleep(2)
        for page in range(self.pages):
            self.swipe_to_left()
            time.sleep(0.1)

    def enter(self):
        return self.click(self.enter_locator)

    def enter_home(self):
        self.guide()
        self.enter()


def enter_home():
    pass

from pages.base import BasePage
from appium.webdriver.common.mobileby import MobileBy as By


class NavPage(BasePage):

    # user_locator = (By.XPATH, '//android.widget.TabWidget[@resource-id=\"android:id/tabs\"]/android.widget.LinearLayout[4]')
    user_locator = (By.ANDROID_UIAUTOMATOR,
                    'new UiSelector().resourceId("com.lemon.lemonban:id/fragment_my_lemon_avatar_image")')

    def user(self):
        return self.click(self.user_locator)

    def eplore(self):
        pass

    # 风格设计，unittest / pytest

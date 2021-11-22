from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base import BasePage


class LoginPage(BasePage):

    mobile_locator = (By.ID, 'com.xxzb.fenwoo:id/et_phone')
    next_locator = (By.ID, 'com.xxzb.fenwoo:id/btn_next_step')
    error_msg_locator = (By.ID, 'com.xxzb.fenwoo:id/tv_message')
    error_msg_confirm_locator = (By.ID, 'com.xxzb.fenwoo:id/btn_confirm')
    mobile_format_error_locator = (By.XPATH, '*[contains(@text, "手机号码格式不正确")]')
    pwd_locator = (By.ID, 'com.xxzb.fenwoo:id/et_pwd')
    cancel_locator = (By.ID, 'com.xxzb.fenwoo:id/btn_cancel')
    # pwd_confirm_locator = ()

    def mobile(self) -> WebElement:
        return self.get_visible_element(self.mobile_locator)

    def send_mobile(self, mobile):
        return self.mobile().send_keys(mobile)

    def click_next(self):
        return self.get_visible_element(self.next_locator).click()

    def get_error_msg(self):
        return self.get_visible_element(self.error_msg_locator)

    def accept_error_toast(self):
        return self.get_visible_element(self.error_msg_confirm_locator).click()

    def toast(self):
        """获取toast"""
        return self.get_presence_element(self.mobile_format_error_locator)

    def send_pwd(self, pwd):
        return self.get_visible_element(self.pwd_locator).send_keys(pwd)

    def login(self, mobile, pwd):
        self.send_mobile(mobile)
        self.click_next()
        self.send_pwd(pwd)
        self.click_next()
        try:
            self.click(self.cancel_locator)
        except:
            pass

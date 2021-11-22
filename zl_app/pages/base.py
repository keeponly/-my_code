from appium.webdriver import Remote
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from helper.keys import Keys


class BasePage:
    def __init__(self, driver):

         self.driver = driver

    def get_visible_element(self, locator, equency=20):
        try:
            return WebDriverWait(self.driver, equency).until(
                ec.visibility_of_element_located(locator))
        except Exception as e:
            self.driver.save_screenshot('test.png')
            # logger.error(e)

    def get_presence_element(self, locator, equency=20):
        try:
            return WebDriverWait(self.driver, equency).until(
                ec.presence_of_element_located(locator))
        except Exception as e:
            self.driver.save_screenshot('test.png')

    def get_clickable_element(self, locator, equency=20):
        try:
            return WebDriverWait(self.driver, equency).until(
                ec.element_to_be_clickable(locator))
        except Exception as e:
            self.driver.save_screenshot('test.png')
            # logger.error(e)

    # def switch_window(self, fqc=20, name=None):
    #     if not name:
    #         handles = self.driver.window_handles
    #         current_handle = self.driver.current_window_handle
    #         WebDriverWait(self.driver, timeout=fqc).until(ec.new_window_is_opened(current_handle))
    #         return self.driver.switch_to.window(handles[-1])
    #     return self.driver.switch_to.window(name)

    def switch_context(self, context=None):
        """切换上下文"""
        #
        # 封装，webview-包名, NATIVE_APP
        # try:
        contexts = self.driver.contexts
        for c in contexts:
            if c == context:
                self.driver.switch_to.context(context)

    @property
    def width(self):
        return self.driver.get_window_size().get('width', 0)

    # 函数颗粒度
    # 函数定义的复杂，使用起来一定方便。
    @property
    def height(self):
        return self.driver.get_window_size().get('height', 0)

    def swipe_to_left(self, offset=0.1):
        """从右到左滑动"""
        return self.driver.swipe(self.width*(1 - offset),
                                 self.height*0.5,
                                 self.width*offset,
                                 self.height*0.5)

    def swipe_to_right(self):
        """从左到右滑动"""
        return self.driver.swipe(self.width * 0.1,
                                 self.height * 0.5,
                                 self.width * (1-0.1),
                                 self.height * 0.5)

    def swipe_to_bottom(self):
        """从上到下滑动"""
        return self.driver.swipe(self.width * 0.5,
                                 self.height * 0.1,
                                 self.width * 0.5,
                                 self.height * (1-0.1))

    def swipe_to_top(self):
        """从下到上滑动"""
        return self.driver.swipe(self.width * 0.5,
                                 self.height * (1-0.1),
                                 self.width * 0.5,
                                 self.height * 0.1)

    def click(self, locator):
        """点击"""
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator)).click()

    def get_toast(self, locator): # alert
        """获取toast"""
        # try:
        e = self.get_presence_element(locator)
        return e.text

    def press_key_power(self):
        """电源键"""
        self.driver.press_keycode(Keys.POWER)
        pass

    def press_home(self):
        """返回到手机首页"""
        pass

    def hide_key_board(self):
        pass
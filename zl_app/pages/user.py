import time

from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy as By
from appium.webdriver.common.touch_action import TouchAction

from pages.base import BasePage


class UserPage(BasePage):
    security_locator = (By.ID, 'com.xxzb.fenwoo:id/textView11')
    gesture_locator = (By.ID, 'com.xxzb.fenwoo:id/layout_gesture_password')
    set_gesture_locator = (By.ID, 'com.xxzb.fenwoo:id/layout_update_gesture')
    create_gesture_locator = (By.ID, 'com.xxzb.fenwoo:id/btn_gesturepwd_guide')
    gester_confirm_locator = (By.ID, 'com.xxzb.fenwoo:id/right_btn')
    gesture_draw_locator = (By.ID, 'com.xxzb.fenwoo:id/gesturepwd_create_lockview')

    def click_security(self):
        return self.get_clickable_element(self.security_locator).click()

    def click_gesture(self):
        return self.get_clickable_element(self.gesture_locator).click()

    def click_set_gesture(self):
        return self.get_clickable_element(self.set_gesture_locator).click()

    def click_create_gesture(self):
        return self.get_clickable_element(self.create_gesture_locator).click()

    def click_confirm_gesture(self):
        return self.get_clickable_element(self.gester_confirm_locator).click()

    def gesture_draw(self) -> WebElement:
        return self.get_visible_element(self.gesture_draw_locator)

    def draw_gesture(self,options):
        drawer = self.gesture_draw()
        rect = drawer.rect
        start_x = rect.get('x')
        start_y = rect.get('y')
        step_x = rect.get('width')/6
        step_y = rect.get('height')/6

        points = ({"x": start_x + step_x, "y": start_y + step_y},
                  {"x": start_x + step_x * 3, "y": start_y + step_y},
                  {"x": start_x + step_x * 5, "y": start_y + step_y},
                  {"x": start_x + step_x, "y": start_y + step_y * 3},
                  {"x": start_x + step_x * 3, "y": start_y + step_y * 3},
                  {"x": start_x + step_x * 5, "y": start_y + step_y * 3},
                  {"x": start_x + step_x, "y": start_y + step_y * 5},
                  {"x": start_x + step_x * 3, "y": start_y + step_y * 5},
                  {"x": start_x + step_x * 5, "y": start_y + step_y * 5})

        action = TouchAction(self.driver)

        action.press(**points[options[0]-1]).wait(200)
        for p in options[1:]:
            action.move_to(**points[p-1]).wait(200)
        action.release().perform()

        # action.press(**points[0]).wait(
        #     200).move_to(**points[1]).wait(
        #     200).move_to(**points[2]).wait(
        #     200).move_to(**points[3]).wait(
        #     200).release().perform()

    def create_gesture(self, options):
        self.click_security()
        self.click_gesture()
        self.click_set_gesture()
        self.click_create_gesture()
        self.click_confirm_gesture()
        self.draw_gesture(options)
        self.click_confirm_gesture()


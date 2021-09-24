
import time
import unittest

import ddt
import win32gui

import win32con
from mgy.pages.page.edit_project import EditProject
from mgy.pages.page.login import LoginPage
from mgy.test_data.project_data import *
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 测试项目信息编辑
# 登录--搜索项目--点击项目
from PycharmProjects.mgy.test_data.project_data import push_project

template = "//a[@href='#/zlpg/template']"
upload_template_ele = "//a[@href='#/zlpg/template/templateFile']"
upload_file_ele = "//span[text() = '+ 上传新文件']"
template_name_ele = "//*[@id='app']/div/div[2]/div[2]/div[3]/div/div[2]/div/div/div/div[1]/form/div[1]/div/div/input"
template_describe_ele = "//*[@id='app']/div/div[2]/div[2]/div[3]/div/div[2]/div/div/div/div[1]/form/div[2]/div/div/textarea"
mark_ele = "//*[@id='app']/div/div[2]/div[2]/div[3]/div/div[2]/div/div/div/div[1]/form/div[3]/div/div/div[1]/input"
add_ele = "//span[text() ='+ 添加']/.."
template_type_ele = "//input[@placeholder='请选择']"
assessment_ele = '//span[text() ="评估说明内容模版"]'
assessment_01_ele ='//*[@id="app"]/div/div[2]/div[2]/div[3]/div/div[2]/div/div/div/div[1]/form/div[5]/div/div/div[2]/div/div[1]/input'
assessment_02_ele = "//span[text() ='材料采购']"


@ddt.ddt
class TestEditPro(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        #cls.driver = Chrome()
        cls.driver = Firefox()
        cls.edit_project = EditProject(cls.driver)
        cls.login_page = LoginPage(cls.driver)
        cls.login_page.login("13611110000", "abc123", "1111")
        time.sleep(3)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @ddt.data(*push_project)
    def test_edit_success(self, data):
        add_template = WebDriverWait(self.driver, 40, 1).until(
            EC.visibility_of_element_located((By.XPATH, template)))
        add_template.click()
        time.sleep(2)
        upload_template = WebDriverWait(self.driver, 40, 1).until(
            EC.visibility_of_element_located((By.XPATH, upload_template_ele)))
        time.sleep(2)
        upload_template.click()


        # 上传新建模板

        upload_file = WebDriverWait(self.driver, 40, 1).until(
            EC.visibility_of_element_located((By.XPATH, upload_file_ele)))
        time.sleep(2)
        upload_file.click()
        time.sleep(2)
        template_name = WebDriverWait(self.driver, 40, 1).until(
            EC.visibility_of_element_located((By.XPATH, template_name_ele)))
        template_name.click()
        template_name.send_keys('说明-' + data)
        template_describe = WebDriverWait(self.driver, 40, 1).until(
            EC.visibility_of_element_located((By.XPATH, template_describe_ele)))
        template_describe.click()
        template_describe.send_keys('说明-' + data)

        # 上传文件
        add = WebDriverWait(self.driver, 40, 1).until(
            EC.visibility_of_element_located((By.XPATH, add_ele)))
        add.click()
        time.sleep(5)

        # 找到对应的窗口
        dialog = win32gui.FindWindow("#32770", "打开")  # 一级窗口
        # 找到窗口
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 二级

        # 操作
        time.sleep(4)
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, "{}.docx".format(data))  # 发送文件路径
        time.sleep(2)
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
        content = template_describe = WebDriverWait(self.driver, 40, 1).until(
            EC.visibility_of_element_located((By.XPATH, '// input[ @ placeholder = "请选择"]')))
        content.click()
        content_01 = WebDriverWait(self.driver, 40, 1).until(
            EC.visibility_of_element_located((By.XPATH, '//span[text()="评估说明内容模版"]')))
        content_01.click()
        time.sleep(3)
        content_02 = WebDriverWait(self.driver, 40, 1).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[3]/div/div[2]/div/div/div/div[1]/form/div[5]/div/div/div[2]/div/div/span/span/i')))
        content_02 .click()
        content_03 = WebDriverWait(self.driver, 40, 1).until(
            EC.visibility_of_element_located((By.XPATH, '//span[text()="{}"]'.format(data))))
        content_03.click()

        mark = WebDriverWait(self.driver, 40, 1).until(
            EC.visibility_of_element_located((By.XPATH, mark_ele)))
        mark.click()
        mark.send_keys('说明 ')
        mark_01 = WebDriverWait(self.driver, 40, 1).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]")))
        mark_01.click()
        save_ele = WebDriverWait(self.driver, 40, 1).until(
            EC.visibility_of_element_located((By.XPATH, "// span[text() = '保存']")))
        save_ele.click()
        time.sleep(5)



if __name__ == '__main__':
    unittest.main()

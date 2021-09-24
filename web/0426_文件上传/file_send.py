import time

import win32gui
import win32con
from selenium.webdriver import Chrome

driver = Chrome()
driver.get("file:///D:/data/%E7%8F%AD%E7%BA%A7/python14/0422_%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0/index.html")

# 定位元素
e = driver.find_element_by_name('myfile').click()

# time.sleep(2)

# 找到对应的窗口
dialog = win32gui.FindWindow("#32770","打开")  #一级窗口
#找到窗口
ComboBoxEx32 = win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)  #二级
comboBox = win32gui.FindWindowEx(ComboBoxEx32,0,"ComboBox",None)   #三级
edit = win32gui.FindWindowEx(comboBox,0,'Edit',None)    #四级
button = win32gui.FindWindowEx(dialog,0,'Button',None)   #四级

#操作
# time.sleep(2)
win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,'D:\\test.xlsx')    #发送文件路径
# time.sleep(2)
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)    #点击打开按钮
# time.sleep(2)

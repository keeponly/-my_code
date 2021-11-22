import time

from selenium.webdriver import Chrome


driver = Chrome()

driver.get('http://www.baidu.com')

time.sleep(3)

# 最小化
driver.minimize_window()

# 最大化
driver.maximize_window()

# 访问豆瓣
driver.get('http://www.douban.com')

# 后退
driver.back()

# 前进
driver.forward()

# 刷新
driver.refresh()

# 获取网页标题
print(driver.title)

# 获取 URL
print(driver.current_url)

# 截屏
driver.save_screenshot('test.png')

# 获取窗口句柄，窗口id, 还有名字。
print(driver.current_window_handle)

# 关闭标签页,当只有一个标签打开的时候， 执行close就相当于额关闭了浏览器。
driver.close()

# 关闭浏览器
driver.quit()
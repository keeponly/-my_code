# _*_coding: utf-8 _*_
# @Time     :2020/10/30  11:09
# @Author   :wangkai
# @tel      :153139292711
# @ File    :无头游览器.py 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

bro = webdriver.Chrome(chrome_options=chrome_options)

bro.get('https://test-pg.cailian.net/#/login')
sleep(3)

print(bro.page_source)
bro.save_screenshot('1.png')

bro.quit()
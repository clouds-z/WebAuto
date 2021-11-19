"""
encoding : utf-8
author : xjz
date : 2021-11-19
purpose : 讲解selenium的常规用法
"""


from selenium import webdriver
from time import sleep


# 使用executable_path参数，指定chrome浏览器驱动的位置
driver = webdriver.Chrome(executable_path=r'D:\python\WebAuto\WebAuto\chromedriver.exe')


# 打开百度首页
driver.get("http://www.baidu.com")
sleep(3)

# 获得输入框ID
inputID = driver.find_element_by_id("kw")
inputID.clear()

inputID.send_keys(u"自动化测试")

driver.find_element_by_id("su").click()

sleep(5)
driver.quit()
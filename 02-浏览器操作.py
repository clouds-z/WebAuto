"""
encoding : utf-8
author : xjz
date : 2021-11-24
purpose : 讲解selenium的浏览器常用操作

注意：

"""

from selenium import webdriver
from time import sleep


# 使用executable_path参数，指定chrome浏览器驱动的位置
driver = webdriver.Chrome(executable_path=r'D:\python\WebAuto\WebAuto\chromedriver.exe')

# 设置浏览器大小(“长”，“宽”)
driver.set_window_size(1250, 650)

# 打开系统地址
driver.get("https://baidu.com")
sleep(3)

# 输入搜索内容，并点击搜索
driver.find_element_by_id("kw").send_keys(u"selenium学习教程")
sleep(3)
driver.find_element_by_id("su").click()
sleep(3)

# 浏览器后退
driver.back()
sleep(3)

# 浏览器前进
driver.forward()
sleep(3)

# 浏览器刷新
driver.refresh()
sleep(3)

# 清除文本
driver.find_element_by_id("kw").clear()
sleep(3)



"""
encoding : utf-8
author : xjz
date : 2021-11-25
purpose : 介绍selenium的鼠标事件

使用鼠标事件，首先必须导入ActionChains包：
from selenium.webdriver.common.action_chains import ActionChains

"""

# 导入webdriver模块
from selenium import webdriver
from time import sleep

# 导入鼠标事件
from selenium.webdriver.common.action_chains import ActionChains


# 打开谷歌浏览器
driver = webdriver.Chrome(executable_path=r'D:\python\WebAuto\WebAuto\chromedriver.exe')

# 设置窗口大小
driver.set_window_size(1250, 650)

# 打开百度
driver.get("https://baidu.com")

# 设置休眠3秒,并刷新页面
sleep(3)
driver.refresh()

element_song = driver.find_element_by_id('kw').send_keys(u"selenium教程")
sleep(3)
element_ci = driver.find_element_by_id('su')
ActionChains(driver).move_to_element(element_song).perform()
# ActionChains(driver).context_click(element_song)

sleep(3)
driver.quit()

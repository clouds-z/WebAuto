"""
encoding : utf-8
author : xjz
date : 2021-12-02
purpose : 对公司的后端系统进行操作
"""


# 导入selenium的webdriver模块
from selenium import webdriver
# 导入time的sleep模块
from time import sleep
# 导入鼠标事件
from selenium.webdriver.common.action_chains import ActionChains


"""
第一步：指定浏览器并输入测试项目地址
"""
# 1、使用executable_path参数，指定chrome浏览器驱动的位置
tester = webdriver.Chrome(executable_path=r'D:\python\WebAuto\WebAuto\chromedriver.exe')
# 2、设置浏览器窗口大小
tester.set_window_size(1250, 650)
# 3、输入测试系统地址
tester.get("https://test-sanitation-biz.deepblueai.com/")
sleep(3)  # 等待3秒


"""
第二步：登录后台系统，输入用户名、密码、点击登录
"""
# 1、输入用户名
tester.find_element_by_class_name('ant-input-lg').send_keys('17788888888')
sleep(2)
# 2、输入密码
tester.find_element_by_xpath('//*[@id="popContainer"]/div/div/div/div[1]/div[2]\
/form/div[1]/div[3]/div[1]/div[3]/div/div/span/span/input').send_keys('a123456')
sleep(2)
# 3、点击登录按钮
tester.find_element_by_class_name('ant-btn-lg').click()
sleep(1)


"""
第三步：选择“账户管理”模块：
1、创建角色
2、创建账户
"""
# 鼠标悬浮在“账户管理”
# 1、定位要操作的元素
right_click = tester.find_element_by_class_name('anticon-user')
# 2、鼠标悬浮在“账户管理”栏
ActionChains(tester).move_to_element(right_click).perform()
# 3、点击“账户管理”模块
right_click.click()
sleep(1)


# 4、进入“角色列表”模块创建角色
tester.find_element_by_xpath('//*[@id="popContainer"]/section/aside/div/ul/li[6]/ul/li[2]/a').click()
tester.find_element_by_class_name('ant-btn ant-btn-primary').click()


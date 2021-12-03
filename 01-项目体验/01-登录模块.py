"""
encoding : utf-8
author : xjz
date : 2021-12-02
purpose : 对登录模块的测试
1、输入正确的用户名及密码
2、未注册手机号登录
3、密码大小写未区分
4、手机号位数限制
5、密码包含空格、特殊字符
6、已删除手机号登录

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
sleep(1)  # 等待3秒


"""
第二步：输入正确的用户名及密码
"""
# 1、输入正确的用户名
tester.find_element_by_class_name('ant-input-lg').send_keys('17788888888')
sleep(1)
# 2、输入正确的密码
tester.find_element_by_xpath('//*[@id="popContainer"]/div/div/div/div[1]/div[2]\
/form/div[1]/div[3]/div[1]/div[3]/div/div/span/span/input').send_keys('a123456')
sleep(1)
# 3、点击登录按钮
tester.find_element_by_class_name('ant-btn-lg').click()
sleep(2)

# 返回上一个页面
tester.back()


"""
第三步：未注册手机号登录
"""
# 1、输入正确的用户名
tester.find_element_by_class_name('ant-input-lg').send_keys('15200000888')
sleep(1)
# 2、输入正确的密码
tester.find_element_by_xpath('//*[@id="popContainer"]/div/div/div/div[1]/div[2]\
/form/div[1]/div[3]/div[1]/div[3]/div/div/span/span/input').send_keys('a123456')
sleep(1)
# 3、点击登录按钮
tester.find_element_by_class_name('ant-btn-lg').click()
sleep(2)

# 返回上一个页面
tester.refresh()
sleep(1)


"""
第四步：密码大小写未区分
"""
# 1、输入正确的用户名
tester.find_element_by_class_name('ant-input-lg').send_keys('15200000888')
sleep(1)
# 2、输入正确的密码
tester.find_element_by_xpath('//*[@id="popContainer"]/div/div/div/div[1]/div[2]\
/form/div[1]/div[3]/div[1]/div[3]/div/div/span/span/input').send_keys('A123456')
sleep(1)
# 3、点击登录按钮
tester.find_element_by_class_name('ant-btn-lg').click()
sleep(2)

# 返回上一个页面
tester.refresh()
sleep(1)


"""
第五步：手机号位数限制
"""
# 1、输入正确的用户名
tester.find_element_by_class_name('ant-input-lg').send_keys('15200000')
sleep(1)
# 2、输入正确的密码
tester.find_element_by_xpath('//*[@id="popContainer"]/div/div/div/div[1]/div[2]\
/form/div[1]/div[3]/div[1]/div[3]/div/div/span/span/input').send_keys('a123456')
sleep(1)
# 3、点击登录按钮
tester.find_element_by_class_name('ant-btn-lg').click()
sleep(2)

# 返回上一个页面
tester.refresh()
sleep(1)

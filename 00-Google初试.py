"""
encoding : utf-8
author : xjz
date : 2021-11-19
purpose : 讲解selenium的常规用法(模拟登录QQ邮箱并操作)

注意：
1、若是定位元素嵌套在 Frame中，需要先进入frame页面中，再去定位，方法：switch_to.frame("id or name")
2、如果定位元素是动态的，可以根据右击选择xpath去定位
"""


from selenium import webdriver
from time import sleep


# 使用executable_path参数，指定chrome浏览器驱动的位置
driver = webdriver.Chrome(executable_path=r'D:\python\WebAuto\WebAuto\chromedriver.exe')


# 打开系统地址
driver.get("https://mail.qq.com")
sleep(2)            # 等待1秒


# 使用switch_to.frame()定位到frame页面
driver.switch_to.frame("login_frame")

# 使用xpath元素去定位
# 用户名
driver.find_element_by_xpath('//*[@id="u"]').send_keys(u"839811794")
sleep(2)
# 密码
driver.find_element_by_xpath('//*[@id="p"]').send_keys(u"199306zy")


# 清除文本内容
# inputID.clear()

# 点击登录按钮
driver.find_element_by_xpath('//*[@id="login_button"]').click()


sleep(5)

# 退出
driver.quit()

#登录进入智慧养老后台
# #正常登录
# from selenium import webdriver
# import time
# driver =webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://jhzc.zhongenyuan.com/homecareadmin/index.html#/")
# driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/form/div[1]/div/div/input').send_keys('13900139000')
# driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/form/div[2]/div/div[1]/div[1]/div/input').send_keys('123456')
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div/button').click()

#用户不存在登录
from selenium import webdriver
import time
driver =webdriver.Chrome()
driver.maximize_window()
driver.get("https://jhzc.zhongenyuan.com/homecareadmin/index.html#/")
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/form/div[1]/div/div/input').send_keys('15007547489')
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/form/div[2]/div/div[1]/div[1]/div/input').send_keys('123456')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div/button').click()

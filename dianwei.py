#登录，进入点位2点位详情页面
#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver =webdriver.Chrome()
driver.maximize_window()
driver.get("http://192.168.0.220:3000/#/login")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div/form/div[5]/div/div/span/button').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="sider"]/li/ul/li[1]/div[1]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="4"]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="sider"]/li/ul/li[1]/ul/li[1]/ul/li[2]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="allmap"]/div/div[1]/div[1]/div[2]/div[2]/span[1]').click()
from selenium import webdriver
import time
driver = webdriver.Chrome()#谷歌浏览器首字母必须大写
driver.get("https://www.baidu.com/")
time.sleep(3)
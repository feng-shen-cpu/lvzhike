#unittest执行用例
import unittest
from selenium import webdriver
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
    def setUp(self):
        self.driver.maximize_window()
        self.driver.get("https://jhzc.zhongenyuan.com/homecareadmin/index.html#/")
        self.driver.implicitly_wait(10)
    def test_01(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/form/div[1]/div/div/input').send_keys('13900139000')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/form/div[2]/div/div[1]/div[1]/div/input').send_keys('123456')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div/button').click()
    def test_02(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/form/div[1]/div/div/input').send_keys('15007547489')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/form/div[2]/div/div[1]/div[1]/div/input').send_keys('123456')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div/button').click()
    def tearDown(self) :
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
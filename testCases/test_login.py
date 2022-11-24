from selenium import webdriver
import pytest, time
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.chrome.service import Service
class Test_001_Login:
    baseurl= "https://admin-demo.nopcommerce.com/"
    username= "admin@yourstore.com"
    password= "admin"

    def test_homePageTitle(self, setup):
        # service= Service("C://Drivers/chromedriver.exe")
        # global driver
        # self.driver= webdriver.Chrome(service=service)
        # self.driver.maximize_window()
        self.driver= setup
        self.driver.get(self.baseurl)
        if self.driver.title == "Your store. Login":
            assert True
        else:
            self.driver.save_screenshot('C:\\Users\\user\\PycharmProjects\\Base\\Screenshots\\'+'test_homePageTitle.png')
            # C:\Users\user\PycharmProjects\Base\Screenshots
        # assert self.driver.title == "Your store. Login", "The title is WORNG!!!"
        self.driver.quit()
        print(self.driver.title)
        assert False, "The LP title is WORNG!!!"

    def test_Login(self, setup):
        # service = Service("C://Drivers/chromedriver.exe")
        # global driver
        # self.driver = webdriver.Chrome(service=service)
        # self.driver.maximize_window()
        self.driver= setup
        self.driver.get(self.baseurl)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            time.sleep(2)
            self.lp.clickLogout()
            self.driver.quit()
        else:
            self.driver.save_screenshot('C:\\Users\\user\\PycharmProjects\\Base\\Screenshots\\'+ 'test_login.png')
            self.driver.quit()
            assert False, "The title after login is wrong!"

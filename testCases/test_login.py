import self as self
from selenium import webdriver
import pytest, time
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.chrome.service import Service
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    # baseurl= "https://admin-demo.nopcommerce.com/"
    # username= "admin@yourstore.com"
    # password= "admin"
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("=========== Test 001 Login =========")
        self.logger.info("============== Verifying homepage title =============")
        # service= Service("C://Drivers/chromedriver.exe")
        # global driver
        # self.driver= webdriver.Chrome(service=service)
        # self.driver.maximize_window()
        self.driver = setup
        self.driver.get(self.baseurl)
        if self.driver.title == "Your store. Login":
            assert True
            self.logger.info("******* Homepage test is passed ********")

        else:
            self.driver.save_screenshot(
                'C:\\Users\\user\\PycharmProjects\\Base\\Screenshots\\' + 'test_homePageTitle.png')
            # C:\Users\user\PycharmProjects\Base\Screenshots
        # assert self.driver.title == "Your store. Login", "The title is WORNG!!!"
        self.driver.quit()
        print(self.driver.title)
        self.logger.error("******** Homepage test is failed !!! ********")

        assert False, "The LP title is WORNG!!!"

    def test_Login(self, setup):
        self.logger.info("########### Verifying login test #################")
        # service = Service("C://Drivers/chromedriver.exe")
        # global driver
        # self.driver = webdriver.Chrome(service=service)
        # self.driver.maximize_window()
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard888 / nopCommerce administration":
            assert True
            self.logger.info("***** Login test is passed *********")
            time.sleep(2)
            self.lp.clickLogout()
            self.driver.quit()
        else:
            self.driver.save_screenshot('C:\\Users\\user\\PycharmProjects\\Base\\Screenshots\\' + 'test_login.png')
            self.driver.quit()
            self.logger.error("********** loging test is failed !!! ************")
            assert False, "The title after login is wrong!"

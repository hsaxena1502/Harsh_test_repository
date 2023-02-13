import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pageobjects.login import login
from utilities.readproperties import Readconfig
from utilities.customlogger import LogGen


class Test_001_login:
    baseurl = Readconfig.getapplicationurl()
    path=".//Testdata/username.xlsx"
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homepagetitle(self):
        self.logger.info("***************Test_001_Login***************")
        self.logger.info("***************Verifying Home Page Title***************")
        self.driver = webdriver.Chrome(executable_path="/Users/harshsaxena/Downloads/chromedriver_mac_arm64")
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        if act_title == "Your store.Login":
            assert True
            self.driver.close()
            self.logger.info("***************Home page title test is passed***************")

        else:
            self.driver.get_screenshot_as_file(".\\Screenshots "+"test_homepagetitle.png")
            self.driver.close()
            self.logger.info("***************Home page title test is failed***************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self):  #adding fixture setup to stop repition of code driver
        self.driver = webdriver.Chrome(executable_path="/Users/harshsaxena/Downloads/chromedriver_mac_arm64")
        self.driver.get(self.baseurl)
        self.lp = login(self.driver)
        self.rows = Xutils.getRowcount(self.path, 'sheet1')
        print("number of rows in excel:", self.rows)

        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopcommerce administration":
            assert True
            self.logger.info("***************Login test is passed***************")
            self.driver.close()
        else:
            self.logger.info("***************Login test is passed***************")
            self.driver.close()
            self.driver.get_screenshot_as_file(".\\Screenshots "+"test_logintitle.png")

            assert False
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pageobjects.login import login
from utilities.readproperties import Readconfig
from utilities.customlogger import LogGen
from utilities import Xutils

class Test_002_login:
    baseurl = Readconfig.getapplicationurl()
    path = ".//Testdata/username.xlsx"


    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_login_ddt(self):  #adding fixture setup to stop repition of code driver
        self.driver = webdriver.Chrome(executable_path="/Users/harshsaxena/Downloads/chromedriver_mac_arm64")
        self.driver.get(self.baseurl)
        self.lp = login(self.driver)

        self.rows = Xutils.getRowcount(self.path, 'sheet1')
        print("number of rows in excel:", self.rows)

        lst_status = []  # empty list variable

        for r in range(2, self.rows + 1):
            self.user = Xutils.readdata(self.path, 'sheet1', r, 1)
            self.password = Xutils.readdata(self.path, 'sheet1', r, 3)
            self.exp = Xutils.readdata(self.path, 'sheet1', r, 5)

            self.lp.setusername(self.user)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)

        act_title = self.driver.title
        exp_title = "Dashboard / nopcommerce administration"

        if act_title == exp_title:
              if self.exp == "Pass":
                self.logger.info("***Passed")
                self.lp.clicklogin()
                lst_status.append("pass")

              elif self.exp == "fail":
                self.logger.info("***failed")
                self.lp.clicklogout()
                lst_status.append("fail")
        elif act_title != exp_title:
            if  self.exp == "Pass":
                self.logger.info("***failed")
                lst_status.append("fail")

            elif self.ex == "fail":
                 self.logger.info("***passed")
                 lst_status.append("pass")

        if "fail" not in lst_status:
            self.logger.info("***login data driven test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("***login data driven test failed")
            self.driver.close()
            assert  False

            self.logger.info("***end data driven TC")
            self.logger.info("***completed TC002")


import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pageobjects.login import login
from utilities.readproperties import Readconfig
from utilities.customlogger import LogGen
import string
import random

class Test_04_addcustomer:
    baseurl = Readconfig.getapplicationurl()
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_searchcustomerbyemail(self,setup):
        self.logger.info("*******Test_04_searchcustomerbyemail*********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = login(self.driver)
        self.lp.setusername(self.user)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.logger.info("*************Login successful*******")

        self.logger.info ("******starting search by email*********")

        self.addcust = add_customer(self.driver)
        self.addcust.clickoncustomermenu()
        self.addcust.clickoncustomersmenuitem()

        self.logger.info ("******starting search by email ID*********")
        searchcust = searchcustomer(self.driver)
        searchcust.setemail("victoria_victoria@nopCommerce.com")
        searchcust.clickonsearch()
        time.sleep(5)
        status = searchcust.searchcustomerbyemail("victoria_victoria@nopCommerce.com")
        status = assert True
        self.logger.info("************TC_04-search by email ID ended************")
        self.driver.close()
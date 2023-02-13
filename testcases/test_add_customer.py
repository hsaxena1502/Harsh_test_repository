import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pageobjects.login import login
from utilities.readproperties import Readconfig
from utilities.customlogger import LogGen
import string
import random
import pytest

class Test_03_addcustomer:
    baseurl = Readconfig.getapplicationurl()
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addcustomer(self,setup):
        self.logger.info("*******Test_003_addcustomer*********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = login(self.driver)
        self.lp.setusername(self.user)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.logger.info("*************Login successful*******")

        self.logger.info("***********Starting Add customer test******")

        self.addcust = add_customer (self.driver)
        self.addcust.clickoncustomermenu()
        self.addcust.clickoncustomersmenuitem()

        self.addcust.add_newbutton()

        self.logger.info("***********Providing customer info********")

        self.email= random_generator() + "@gmail.com"
        self.addcust.setemail(self.email)
        self.addcust.setpassword("test123")
        self.addcust.setcustomerroles("Guests")
        self.addcust.manager_of_vendor("Vendor 2")
        self.addcust.selectGender("Male")
        self.addcust.setfirstname("Harsh")
        self.addcust.setlastname("saxena")
        self.addcust.setdob("15/02/1994")
        self.addcust.setcompanyname("QAtest")
        self.addcust.setadmincontent("This is for testing")
        self.addcust.clickonsave()
        self.logger.info("*******saving customer info")
        self.logger.info("******Add customer info*********")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text

        print(self.msg)
        if 'customer has been added successfully' in self.msg:
            assert True == True
            self.logger.info("*********Add customer test passed******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addcustomer_scr.png")
            self.logger.error("*********Add customer test failed****")
            assert True == False
        self.driver.close()
        self.logger.info("*******ending home page title test*********")
  ##### random email generator############
def random_generator(size =8, chars= string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


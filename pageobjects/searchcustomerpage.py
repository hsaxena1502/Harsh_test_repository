import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pageobjects.login import login
from utilities.readproperties import Readconfig
from utilities.customlogger import LogGen
import string
import random



class searchcustomer:

    txtEmail_id = "SearchEmail"
    txtfirstname_id = "SearchFirstName"
    txtlastname_id = "SearchLastName"
    btnsearch_id= "search-customers"
    tble_xpath= "//table[@id='customers-grid']"
    tblerows_xpath= "//table[@id='customers-grid']//tbody/tr"
    tblecolumns_xpath= "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver

    def __init__(self,email):
        self.driver.find_element(By.ID, self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def setfirstname(self,fname):
        self.driver.find_element(By.ID, self.txtfirstname_id).clear()
        self.driver.find_element(By.ID, self.txtfirstname_id).send_keys(fname)

    def setlastname(self,lname):
        self.driver.find_element(By.ID, self.txtlastname_id).clear()
        self.driver.find_element(By.ID, self.txtlastname_id).send_keys(lname)

    def clicksearch(self):
        self.driver.find_element(By.XPATH, self.btnsearch_id).click()

    def getnoofrows(self):
        return len(self.driver.find_element(By.XPATH, self.tblerows_xpath))

    def getnoofcolumns(self):
        return len(self.driver.find_element(By.XPATH, self.tblecolumns_xpath))

    def searchcustomerbyemail(self,email):
        flag= False
        for r in range (1,self.getnoofrows()+1):
            table= self.driver.find_element(By.XPATH,self.tble_xpath)
            emailid= table.find.element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid==email:
                flag=True
                break
            return flag

    def searchcustomerbyname(self, Name):
        flag = False
        for r in range (1,self.getnoofrows()+1):
            table= self.driver.find_element(By.XPATH,self.tble_xpath)
            name= table.find.element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag =True
                break
            return flag








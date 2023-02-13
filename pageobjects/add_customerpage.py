import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class add_customer:
    lnkcustomers_menu_Xpath = "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]/p[1]"
    lnkcustomers_menuitem_xpath = "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/p[1]"
    btnaddnew_xpath = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]/i[1]"
    #new customer
    txtemail_xpath = "//input[@id='Email']"
    txtpassword_xpath ="//input[@id='Password']"
    txtfirst_name_xpath = "//input[@id='FirstName']"
    txtlast_name_xpath = "//input[@id='LastName']"
    choicegender_male_xpath = "//label[contains(text(),'Male')]"
    choicegender_female_xpath = "//label[contains(text(),'Female')]"
    txtdob_xpath = "//input[@id='DateOfBirth']"
    txtcompany_name ="//input[@id='Company']"
    choice_tax_exempt_xpath = "//input[@id='IsTaxExempt']"
    dropdown_newsletter_xpath = "//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div[1]"
    dropdown_newsletter_yourstorename_xpath = "//li[@id='334717d9-b14c-41aa-a634-957a3ee8380d']"
    dropdown_newsletter_teststore2_xpath= "//li[contains(text(),'Test store 2')]"
    txtcustomerroles_xpath = "//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]"
    txtcustomerroles_administrators_xpath = "//li[contains(text(),'Administrators')]"
    txtcustomerroles_forummoderators_xpath = "//li[contains(text(),'Forum Moderators')]"
    txtcustomerroles_guests_xpath = "//li[contains(text(),'Guests')]"
    txtcustomer_registered_xpath = "//li[@id='a0146da0-b5b7-4ffa-927c-b0f4b1564a54']"
    txtcustomerroles_vendors_xpath = "//li[@id='a0146da0-b5b7-4ffa-927c-b0f4b1564a54']"
    dropdown_managerofvendor_xpath ="//select[@id='VendorId']"
    dropdown_managerofvendor_choice1_xpath = "//*[@id='VendorId']/option[1]"
    dropdown_managerofvendor_choice1_xpath = "//*[@id='VendorId']/option[2]"
    dropdown_managerofvendor_choice2_xpath = "//*[@id='VendorId']/option[3]"
    choice_active_xpath = "//input[@id='Active']"
    txtadmincomment_xpath = "//textarea[@id='AdminComment']"
    btnsave_xpath = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/button[1]/i[1]"


    #constructor

    def __init__(self,driver):
        self.driver = driver

    def clickoncustomermenu(self):
        self.driver.find_element(By.Xpath, self.lnkcustomers_menu_Xpath).click()

    def clickoncustomersmenuitem(self):
        self.driver.find_element(By.XPATH, self.lnkcustomers_menuitem_xpath).click()

    def add_newbutton(self):
        self.driver.find_element(By.Xpath, self.btnaddnew_xpath).click()

    def addemail(self):
        self.driver.find_element(By.XPATH, self.txtemail_xpath).send_keys(email)

    def addpassword(self):
        self.driver.find_element(By.XPATH, self.txtpassword_xpath).send_keys(password)

    def firstname(self):
        self.driver.find_element(By.XPATH, self.txtfirst_name_xpath).send_keys(first_name)

    def lastname(self):
        self.driver.find_element(By.XPATH, self.txtlast_name_xpath).send_keys(last_name)

    def selectgender_male(self):
        self.driver.find_element(By.XPATH, self.choicegender_male_xpath).click()

    def selectgender_female(self):
        self.driver.find_element(By.XPATH, self.choicegender_female_xpath).click()

    def dob(self):
        self.driver.find_element(By.XPATH, self.txtdob_xpath).click()

    def companyname(self):
        self.driver.find_element(By.XPATH, self.txtcompany_name).click()

    def istaxexempt(self):
        self.driver.find_element(By.XPATH, self.choice_tax_exempt_xpath).click()

    def newsletter(self):
        self.driver.find_element(By.XPATH, self.dropdown_newsletter_xpath).click()

    def customerroles(self):
        self.driver.find_element(By.XPATH, self.txtcustomerroles_xpath).click()
        time.sleep(4)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.txtcustomer_registered_xpath)
        elif role =='Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.txtcustomerroles_administrators_xpath)
        elif role == 'Guests':
            self.listitem = self.driver.find_element(By.XPATH, self.txtcustomerroles_guests_xpath)
        ##here user can be registered or guets, so selection code :
            time.sleep(4)
            self.driver.find_element(By.XPATH,'//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/span[2]').click()
            self.listitem = self.driver.find_element(By.XPATH, self.txtcustomerroles_guests_xpath)

        elif role == 'Registered':
             self.listitem = self.driver.find_element(By.XPATH, self.txtcustomer_registered_xpath)
        elif role== 'Vendors':
           self.listitem = self.driver.find_element(By.XPATH, self.dropdown_managerofvendor_xpath)
        else:
           self.listitem = self.driver.find_element(By.XPATH, self.txtcustomerroles_guests_xpath)
        time.sleep(4)
        self.driver.execute_script("argument[0].click();",self.listitem)



    def manager_of_vendor(self):
        drp= self.driver.find_element(By.XPATH, self.dropdown_managerofvendor_xpath).click()
        drp.select_by_visible_text(value)

    def choose_active(self):
        self.driver.find_element(By.XPATH, self.choicegender_male_xpath).click()

    def admin_comment(self):
        self.driver.find_element(By.XPATH, self.txtadmincomment_xpath).click()

    def button_save(self):
        self.driver.find_element(By.XPATH, self.btnsave_xpath).click()









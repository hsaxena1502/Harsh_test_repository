from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class login:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_Xpath = "//button[contains(text(),'Log in')]"
    link_logout_linktext = "Logout"

    def __int__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH, self.button_login_Xpath).click()

    def clicklogin(self):
        self.driver.find_element(By.LINK_TEXT, self.button_login_Xpath).click()
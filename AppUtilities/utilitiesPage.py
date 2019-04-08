'''
Created on Apr 8, 2019

@author: Anisha
'''
from PageRepository.loginPageRepository import loginPageRepo 

class LoginPageMethods():
    
    def __init__(self, driver):
        self.driver = driver
        self.username_textboxById = loginPageRepo.username_textboxById
        self.password_textboxById = loginPageRepo.password_textboxById
        self.loginButton_byxpath = loginPageRepo.loginButton_byxpath
        
    def typeUserName(self, usrname):
        self.driver.find_element_by_id(self.username_textboxById).clear()
        self.driver.find_element_by_id(self.username_textboxById).send_keys(usrname)
        
    def typePassword(self, pswrd):
        self.driver.find_element_by_id(self.password_textboxById).clear()
        self.driver.find_element_by_id(self.password_textboxById).send_keys(pswrd)
        
    def clickLoginButton(self):
        self.driver.find_element_by_xpath(self.loginButton_byxpath).click()
        
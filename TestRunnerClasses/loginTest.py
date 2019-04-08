'''
Created on Apr 8, 2019

@author: Anisha
'''

from selenium import webdriver
import time   
import unittest
from AppUtilities.utilitiesPage import LoginPageMethods
from AppUtilities.propertyFileConnectivity import propReaderClass

class Login(unittest.TestCase):
    
    prop = propReaderClass().read_propertyFile('config.properties') 

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path= cls.prop.get('path'))
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
    
        
    def test_login_case(self):
        driver = self.driver
        prop = self.prop
        driver.get(prop.get('url'))
        time.sleep(2)
        
        login = LoginPageMethods(driver)
        login.typeUserName(prop.get('userNme'))
        login.typePassword(prop.get('psword'))
        login.clickLoginButton()
        time.sleep(2)
        
        text = "The user or password is incorrect."
        errorMessage = self.driver.execute_script("return arguments[0].innerHTML;",self.driver.find_element_by_xpath("//span[@class='warning']"))
        print(errorMessage)
        
        if text in errorMessage:
            input("Got the error message on the login page ")
        else: 
            input("error message not received")
    
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Negative test scenario validated")



from selenium.webdriver.common.keys import Keys
from SearchFB import SearchFB

class LoginFB:
    def __init__(self, driver):
        self.username = 'seuemail'
        self.password = 'suasenha'
        self.driver = driver

    def login(self):
        try:
            usernameElem = self.driver.find_element_by_id('email')
            passwordElem = self.driver.find_element_by_id('pass')

            usernameElem.send_keys(self.username)
            passwordElem.send_keys(self.password, Keys.RETURN)

            print("login success!")
            
        except:
            print("login error!")
            self.login()
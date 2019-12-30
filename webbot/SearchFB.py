from selenium.webdriver.common.keys import Keys

class SearchFB:
    def __init__(self, driver):
        self.driver = driver

    def query(self, param):
        try:
            bodyOpacity = self.driver.find_element_by_class_name('_3ixn')
            bodyOpacity.click()
            searchBtn = self.driver.find_elements_by_css_selector('._42ft._4jy0._4w98._4jy3._517h._51sy')
            self.driver.execute_script('document.querySelector("._1frb").value = "' + param + '"') #Query
            searchBtn[0].click()
            print('query success!')
        except:
            print('query error!')
            self.query(param)
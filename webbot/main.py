from LoginFB import LoginFB
from SearchFB import SearchFB
from selenium import webdriver

BASE_URL = 'https://www.facebook.com/'
driver = webdriver.Chrome()
facebook = LoginFB(driver)
search = SearchFB(driver)

driver.get(BASE_URL)
facebook.login()
search.query('Super Nintendo')
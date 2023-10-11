import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Test_URL_Login:

    def test_URL_Validation(self):
        driver = webdriver.Chrome()
        driver.get('https://www.saucedemo.com/')
        if driver.title == "Swag Labs":
            assert True
        else:
            assert False

    def test_login_002(self):
        driver = webdriver.Chrome()
        driver.get('https://www.saucedemo.com/')
        driver.find_element(By.ID, 'user-name').send_keys("standard_user")
        driver.find_element(By.ID, 'password').send_keys("secret_sauce")
        driver.find_element(By.ID, 'login-button').click()
        try:
            driver.find_element(By.XPATH, '//span[@class="title"]')
            login = True
        except NoSuchElementException:
            login = False
            pass
        time.sleep(5)
        if login == True:
            driver.find_element(By.ID, 'react-burger-menu-btn').click()
            driver.find_element(By.ID, 'logout_sidebar_link').click()
            assert True
        else:
            assert False





import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Test_URL_Login:

    def test_URL_Validation(self, setup):
        self.driver = setup
        if self.driver.title == "Swag Labs":
            assert True
        else:
            assert False

    def test_login_002(self, setup):
        self.driver = setup
        self.driver.find_element(By.ID, 'user-name').send_keys("standard_user")
        self.driver.find_element(By.ID, 'password').send_keys("secret_sauce")
        self.driver.find_element(By.ID, 'login-button').click()
        try:
            self.driver.find_element(By.XPATH, '//span[@class="title"]')
            login = True
        except NoSuchElementException:
            login = False
            pass
        time.sleep(5)
        if login == True:
            self.driver.find_element(By.ID, 'react-burger-menu-btn').click()
            self.driver.find_element(By.ID, 'logout_sidebar_link').click()
            assert True
        else:
            assert False



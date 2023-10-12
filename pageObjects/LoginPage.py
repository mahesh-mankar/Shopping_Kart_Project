
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Login:

    Text_Username = (By.ID, 'user-name')
    Text_Password = (By.ID, 'password')
    Click_Login_Button = (By.ID, 'login-button')
    Dashboard_PageTitle = (By.XPATH, '//span[@class="title"]')
    Menu_Button = (By.ID, 'react-burger-menu-btn')
    Logout_Button = (By.ID, 'logout_sidebar_link')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        self.wait.until(expected_conditions.presence_of_element_located(self.Text_Username))
        self.driver.find_element(*Login.Text_Username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*Login.Text_Password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*Login.Click_Login_Button).click()

    def login_status(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located(self.Dashboard_PageTitle))
            self.driver.find_element(*Login.Dashboard_PageTitle)
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def click_menu_button(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.Menu_Button))
        self.driver.find_element(*Login.Menu_Button).click()

    def click_logout_button(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.Logout_Button))
        self.driver.find_element(*Login.Logout_Button).click()


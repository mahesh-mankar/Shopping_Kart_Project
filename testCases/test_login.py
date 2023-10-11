
from pageObjects.LoginPage import Login
from utilities.Readconfigfile import ReadValues
from utilities.Logger import LogGen


class Test_URL_Login:
    url = ReadValues.getUrl()
    username = ReadValues.getUsername()
    password = ReadValues.getPassword()
    log = LogGen.loggen()

    def test_URL_Validation(self, setup):
        self.log.info("Opening Browser")
        self.driver = setup
        self.log.info("Go to url")
        self.driver.get(self.url)
        self.log.info("Checking page title")
        if self.driver.title == "Swag Labs":
            self.log.info("test_URL_Validation is Pass")
            self.driver.save_screenshot("C:\\Users\\LENOVO\\PycharmProjects\\pythonProject\\Shopping_Kart\\Screenshots\\test_URL_Validation_Pass.png")
            assert True
        else:
            self.log.info("test_URL_Validation is Failed")
            self.driver.save_screenshot("C:\\Users\\LENOVO\\PycharmProjects\\pythonProject\\Shopping_Kart\\Screenshots\\test_URL_Validation_Fail.png")
            assert False
        self.log.info("test_URL_Validation is Completed")
        self.driver.close()
        self.log.info("Browser closed")

    def test_login_002(self, setup):
        self.log.info("Opening Browser")
        self.driver = setup
        self.log.info("Go to url")
        self.driver.get(self.url)
        self.log.info("opening login page")
        self.lp = Login(self.driver)
        self.log.info("Enter username")
        self.lp.enter_username(self.username)
        self.log.info("Enter password")
        self.lp.enter_password(self.password)
        self.log.info("Click on login button")
        self.lp.click_login()
        if self.lp.login_status() == True:
            self.log.info("test_login_002 is Pass")
            self.driver.save_screenshot("C:\\Users\\LENOVO\\PycharmProjects\\pythonProject\\Shopping_Kart\\Screenshots\\test_login_002_Pass.png")
            self.log.info("Click on menu button")
            self.lp.click_menu_button()
            self.log.info("Click on logout button")
            self.lp.click_logout_button()
            assert True
        else:
            self.log.info("test_login_002 is Failed")
            self.driver.save_screenshot("C:\\Users\\LENOVO\\PycharmProjects\\pythonProject\\Shopping_Kart\\Screenshots\\test_login_002_Fail.png")
            assert False
        self.log.info("test_login_002 is completed")
        self.driver.close()
        self.log.info("Browser closed")


from pageObjects.LoginPage import Login
from utilities.Readconfigfile import ReadValues


class Test_URL_Login:
    username = ReadValues.getUsername()
    password = ReadValues.getPassword()

    def test_URL_Validation(self, setup):
        self.driver = setup
        if self.driver.title == "Swag Labs":
            self.driver.save_screenshot("C:\\Users\\LENOVO\\PycharmProjects\\pythonProject\\Shopping_Kart\\Screenshots\\test_URL_Validation_Pass.png")
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\LENOVO\\PycharmProjects\\pythonProject\\Shopping_Kart\\Screenshots\\test_URL_Validation_Fail.png")
            assert False

    def test_login_002(self, setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        if self.lp.login_status() == True:
            self.driver.save_screenshot("C:\\Users\\LENOVO\\PycharmProjects\\pythonProject\\Shopping_Kart\\Screenshots\\test_login_002_Pass.png")
            self.lp.click_menu_button()
            self.lp.click_logout_button()
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\LENOVO\\PycharmProjects\\pythonProject\\Shopping_Kart\\Screenshots\\test_login_002_Fail.png")
            assert False

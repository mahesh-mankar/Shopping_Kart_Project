import time

from pageObjects.LoginPage import Login


class Test_URL_Login:

    def test_URL_Validation(self, setup):
        self.driver = setup
        if self.driver.title == "Swag Labs":
            assert True
        else:
            assert False

    def test_login_002(self, setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.enter_username("standard_user")
        self.lp.enter_password("secret_sauce")
        self.lp.click_login()
        time.sleep(5)
        if self.lp.login_status() == True:
            self.lp.click_menu_button()
            self.lp.click_logout_button()
            assert True
        else:
            assert False

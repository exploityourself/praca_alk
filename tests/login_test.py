from tests.base_test import BaseTest
from time import sleep

class LogInTest(BaseTest):

    def test_login(self):
        """
        TC01 Test verifies successful login
        """
        self.driver.implicitly_wait(10)
        self.home_page.click_login_link()
        self.driver.implicitly_wait(10)
        self.login_page.input_username(self.test_data.username)
        self.login_page.input_password(self.test_data.password)
        self.login_page.click_login_button()
        sleep(4)
        self.assertEqual(self.home_page.get_welcomed(), "Welcome asd")



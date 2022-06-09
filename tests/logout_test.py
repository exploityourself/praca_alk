from tests.base_test import BaseTest
from time import sleep

class LogOutTest(BaseTest):

    def test_logout(self):
        """
        TC02 Test verifies successful logout after user is logged in
        """
        self.driver.implicitly_wait(10)
        self.home_page.click_login_link()
        self.driver.implicitly_wait(10)
        self.login_page.input_username(self.test_data.username)
        self.login_page.input_password(self.test_data.password)
        self.login_page.click_login_button()
        sleep(4)
        # Test starts here, after preconditions are fulfilled
        self.home_page.click_logout_button()
        # If user logged out, there should be login link available
        self.assertEqual(self.home_page.get_login(), "Log in")


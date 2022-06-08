from tests.base_test import BaseTest


class LogInTest(BaseTest):

    def successful_login(self):
        """
        TC01 Test case verifies successful login of registered user
        """
        self.home_page.click_login_link()
        self.login_page.input_username()
        self.login_page.input_password()
        self.login_page.click_login_button()
        self.home_page.verify_welcome_user()
        
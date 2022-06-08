from tests.base_test import BaseTest


class LogInTest(BaseTest):

    def login_and_logout(self):
        """
        TC02 Tests verify successful logout after user is logged in
        """
        self.home_page.click_login_link()
        self.home_page.input_username()
        self.home_page.input_password()
        self.home_page.click_login_button()
        self.home_page.click_logout_link()
        # If user logged out, there should be login link available
        self.home_page.click_login_link()

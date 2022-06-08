from tests.base_test import BaseTest


class LogInTest(BaseTest):

    def logout(self):
        """
        TC02 Tests verify successful logout after user is logged in
        """
        self.home_page.click_login_link()
        self.home_page.input_username()
        self.home_page.input_password()
        self.home_page.click_login_button()
        self.home_page.click_logout_link()
        self.home_page.verify_user_logout()

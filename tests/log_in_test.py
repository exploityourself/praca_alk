from tests.base_test import BaseTest


class LogInTest(BaseTest):
    def successful_login(self):
        self.home_page.click_login_link()
        self.home_page.input_username()
        self.home_page.input_password()
        self.home_page.click_login_button()
        self.home_page.verify_welcome_user()

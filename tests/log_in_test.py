from tests.base_test import BaseTest


class LogInTest(BaseTest):

    def successful_login(self):
        self.home_page.click_sign_in

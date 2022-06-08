import unittest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.galaxy_s6_page import GalaxyS6Page
from pages.cart_page import CartPage

from selenium import webdriver


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com")
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.galaxy_s6_page = GalaxyS6Page(self.driver)
        self.cart_page = CartPage(self.driver)

    def tearDown(self):
        self.driver.quit()

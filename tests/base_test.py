from pages.home_page import HomePage
from pages.galaxy_s6_page import GalaxyS6Page
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.place_order_page import PlaceOrderPage

from tests.test_data import TestData

from selenium import webdriver
import unittest


class BaseTest(unittest.TestCase):
    """
    Base class for tests
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/")
        self.driver.implicitly_wait(10)
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.galaxy_s6_page = GalaxyS6Page(self.driver)
        self.cart_page = CartPage(self.driver)
        self.place_order_page = PlaceOrderPage(self.driver)
        self.test_data = TestData()

    def tearDown(self):
        self.driver.quit()

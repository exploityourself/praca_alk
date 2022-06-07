import unittest
from pages.home_page import HomePage
from selenium import webdriver


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com")
        self.home_page = HomePage(self.driver)
    def tearDown(self):
        self.driver.quit()

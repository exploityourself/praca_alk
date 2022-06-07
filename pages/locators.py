from selenium.webdriver.common.by import By


class HomePageLocators():
    LOG_IN_LINK = (By.ID, "login2")
    USERNAME = (By.ID, "loginusername")
    PASSWORD = (By.ID, "loginpassword")
    LOG_IN_BUTTON = (By.CLASS, "btn btn-primary")
    WELCOME_USERNAME = (By.ID, "nameofuser")
    SAMSUNG_GALAXY_S6 = (By.LINKTEXT, "Samsung galaxy s6")

class GalaxyS6PageLocators():
    ADD_TO_CART = (By.CLASS, "(By.CLASS, "btn btn-primary")")
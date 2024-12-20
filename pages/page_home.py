from pages.basePage import BasePage
from locators.homePageLocators import HomePageLocators
from selenium.webdriver.common.keys import Keys


class HomePage(BasePage):
    def enter_distance(self, value):
        self.type_text(*HomePageLocators.Distance, value)


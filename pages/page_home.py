from pages.basePage import BasePage
from locators.homePageLocators import HomePageLocators
from selenium.webdriver.common.keys import Keys


class HomePage(BasePage):
    def enter_distance(self, value):
        self.type_text(*HomePageLocators.Distance, value)

    def set_departure(self, month, day, year):
        """
        Sets the start time by interacting with the datetime-local input field.

        :param month: The month to set (e.g., "12").
        :param day: The day to set (e.g., "20").
        :param year: The year to set (e.g., "2024").

        """

        # Format date-time string for input
        date_time_str = f"{month}-{day}-{year}"

        # Input the formatted date-time string
        self.click_element(*HomePageLocators.DEPARTURE_DATE)
        self.driver.find_element(*HomePageLocators.DEPARTURE_DATE).clear()
        self.driver.find_element(*HomePageLocators.DEPARTURE_DATE).send_keys(date_time_str)

    def select_service_class(self, value):
        self.select_dropdown_option_by_value(*HomePageLocators.SERVICE_CLASS, value)

    def enter_ticket_number(self,value):
        self.type_text(*HomePageLocators.TICKET,value)

    def get_actual_error_message_for_ticket(self):
        return self.get_element_text(*HomePageLocators.ERROR_MESSAGE_TICKET)
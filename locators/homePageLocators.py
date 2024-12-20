from selenium.webdriver.common.by import By


class HomePageLocators:
    def __init__(self):
        pass

    Distance = (By.CSS_SELECTOR, "input#distance")
    DEPARTURE_DATE = (By.CSS_SELECTOR, "input#departureDate")
    SERVICE_CLASS = (By.CSS_SELECTOR, "select#serviceClass")
    TICKET = (By.CSS_SELECTOR, "input#numberOfTickets")
    ERROR_MESSAGE_TICKET = (By.CSS_SELECTOR, "div#result")


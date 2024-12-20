from pages.basePage import BasePage
from pages.page_home import HomePage


def test_economy(setup):
    basePage = BasePage(setup)
    basePage.navigate_to_url("https://muntasir101.github.io/Ticket-Fare/")

    home_page = HomePage(setup)
    home_page.enter_distance("100")


def test_business(setup):
    basePage = BasePage(setup)
    basePage.navigate_to_url("https://muntasir101.github.io/Ticket-Fare/")

    home_page = HomePage(setup)
    home_page.enter_distance("500")


def test_first(setup):
    basePage = BasePage(setup)
    basePage.navigate_to_url("https://muntasir101.github.io/Ticket-Fare/")

    home_page = HomePage(setup)
    home_page.enter_distance("1500")

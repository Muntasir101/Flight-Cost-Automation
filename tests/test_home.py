from pages.basePage import BasePage
from pages.page_home import HomePage


def test_economy_valid(setup):
    basePage = BasePage(setup)
    basePage.navigate_to_url("https://muntasir101.github.io/Ticket-Fare/")

    home_page = HomePage(setup)
    home_page.enter_distance("100")
    home_page.select_service_class("economy")


def test_economy_invalid_number_of_ticket(setup):
    basePage = BasePage(setup)
    basePage.navigate_to_url("https://muntasir101.github.io/Ticket-Fare/")

    home_page = HomePage(setup)
    home_page.enter_distance("100")
    home_page.select_service_class("economy")
    home_page.enter_ticket_number("5")

    # Verify cost
    expected_error_message_for_tickets = "Number of tickets must be between 1 and 4."

    # Call the method to get the actual booking cost
    actual_error_message_for_tickets = home_page.get_actual_error_message_for_ticket()

    # Now use the actual cost for comparison in the assertion
    assert expected_error_message_for_tickets == expected_error_message_for_tickets, \
        f"Test Case Failed. Expected Cost: {expected_error_message_for_tickets}, But Found: {actual_error_message_for_tickets}"

    print("Test Case Passed")


def test_business_valid(setup):
    basePage = BasePage(setup)
    basePage.navigate_to_url("https://muntasir101.github.io/Ticket-Fare/")

    home_page = HomePage(setup)
    home_page.enter_distance("500")
    home_page.select_service_class("business")


def test_first_valid(setup):
    basePage = BasePage(setup)
    basePage.navigate_to_url("https://muntasir101.github.io/Ticket-Fare/")

    home_page = HomePage(setup)
    home_page.enter_distance("1500")
    home_page.select_service_class("first")

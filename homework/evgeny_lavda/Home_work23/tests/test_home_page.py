from page.home_page import HomePage


def test_search_alert_message(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_search_button()
    assert home_page.alert_message()

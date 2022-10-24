from pages.home_page import HomePage
from pages.our_stores_page import OurStore
from time import sleep
import pytest

CREDENTIALS = ['Minsk', 'Miami', 'Brazil', 'Spain']


@pytest.mark.parametrize('location', CREDENTIALS)
def test_our_stores(driver, location):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.click_footer_our_stores()
    sleep(3)    # for demonstration purposes
    our_store_page = OurStore(driver)
    our_store_page.enter_your_location(location)
    assert our_store_page.check_that_alert_is_displayed(location)


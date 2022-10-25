from pages.home_page import HomePage
from pages.our_stores_page import OurStore
from time import sleep
import pytest

CREDENTIALS = ['15', '25', '50', '100']


@pytest.mark.parametrize('radius', CREDENTIALS)
def test_our_stores(driver, radius):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.click_footer_our_stores()
    sleep(3)    # for demonstration purposes
    our_store_page = OurStore(driver)
    our_store_page.enter_your_location_data(location='Hollywood')
    our_store_page.select_radius(radius=radius)
    our_store_page.click_search_button()
    assert our_store_page.check_that_alert_message_is_displayed(location='Hollywood')



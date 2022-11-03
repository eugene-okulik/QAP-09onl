import pytest
from pages.home_page import HomePage
from pages.stores_page import StoresPage

TEST_DATA = ['15', '25', '50', '100']


@pytest.mark.parametrize('radius', TEST_DATA)
def test_search_location_error(driver, radius):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.scroll_page_to_bottom()
    home_page.click_stores_button()
    stores_page = StoresPage(driver)
    stores_page.your_location_search('Hollywood', radius)
    assert stores_page.check_error()

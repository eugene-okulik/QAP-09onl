from pages.stores_page import OurStores
import allure


@allure.feature('information section')
@allure.story('stores')
def test_stores(driver):
    stores = OurStores(driver)
    stores.open_page()
    stores.click_our_stores()
    assert 'OUR STORE(S)!' in stores.check_heading_text()

from pages.stores_page import OurStores


def test_stores(driver):
    stores = OurStores(driver)
    stores.open_page()
    stores.click_our_stores()
    assert 'OUR STORE(S)!' in stores.check_heading_text()

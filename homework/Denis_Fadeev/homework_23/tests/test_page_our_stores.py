from pages.our_stores import OurStores


def test_page_our_stores(driver):
    our_stores = OurStores(driver)
    our_stores.open_page()
    our_stores.click_button_ok_on_map()
    our_stores.search_location('Moscow')

from pages.our_stores_page import OurStoresPage


def test_our_stores(chrome_driver):
    our_stores = OurStoresPage(chrome_driver)
    our_stores.open_our_stores_page()
    assert our_stores.check_our_stores_text()
    print(our_stores.check_our_stores_text())
    assert our_stores.check_button_ok()
    print(our_stores.check_button_ok())
    our_stores.click_button_ok()
    assert our_stores.check_button_search()
    print(our_stores.check_button_search())




import code_for_test_hw_23 as cfth2


def test_best_sellers(driver):
    print('/// testing open best sellers ///')
    cfth2.open_best_sellers(driver)

    add_to_compare_button = cfth2.find_add_to_compare(driver)
    add_to_compare_button.click()

    compare = cfth2.find_compare(driver)

    cfth2.check_compare(compare, driver)


def test_our_stores(driver):
    print('/// testing open our stores ///')
    cfth2.open_our_stores(driver)

    search_button = cfth2.find_search_box(driver)

    assert search_button.is_displayed()


def test_about_us(driver):
    print('/// testing open about us ///')
    cfth2.open_about_us(driver)

    our_company = cfth2.find_our_company(driver)

    assert our_company.text == 'OUR COMPANY'



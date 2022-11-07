import pytest
from pages.home_page import HomePage
from pages.best_sellers_page import BestSellers
from pages.about_us_page import AboutUs
from pages.our_stores import OurStores
import ast


class TestHomePage:
    def test_go_to_best_sellers_page(self, driver):
        """check out a clickable 'bestsellers' link and successful transition on the bestsellers page"""
        home_page = HomePage(driver)
        home_page.open_page()
        home_page.scroll_page_to_bottom()
        home_page.click_best_sellers_link()
        assert "http://automationpractice.com/index.php?controller=best-sales" == home_page.find_current_url()

    def test_go_to_about_us_page(self, driver):
        """check out a clickable 'about us' link and successful transition on the about_us page"""
        home_page = HomePage(driver)
        home_page.open_page()
        home_page.scroll_page_to_bottom()
        home_page.click_about_us_link()
        assert "http://automationpractice.com/index.php?id_cms=4&controller=cms" == home_page.find_current_url()

    def test_go_to_our_stores_page(self, driver):
        """check out a clickable 'our stores' link and successful transition on the our_store page"""
        home_page = HomePage(driver)
        home_page.open_page()
        home_page.scroll_page_to_bottom()
        home_page.click_our_stores_link()
        assert "http://automationpractice.com/index.php?controller=stores" == home_page.find_current_url()


class TestBestSellersPage:

    def test_decreasing_sort_by_name(self, driver):
        """check out an items sort by "Product Name: Z to A" on the best_sellers_page"""
        best_sellers_page = BestSellers(driver)
        best_sellers_page.open_page()
        before_items = best_sellers_page.find_internal_text()  # the items name list before sorting
        best_sellers_page.select_dropdown("Product Name: Z to A")  # check out drop-down menu on the best_sellers_page
        after_items = best_sellers_page.find_internal_text()  # the items name list after sorting
        assert sorted(before_items, reverse=True) == after_items

    def test_delivery_info(self, driver):
        """check out the delivery information"""
        best_sellers_page = BestSellers(driver)
        best_sellers_page.open_page()
        best_sellers_page.scroll_page_to_bottom()
        best_sellers_page.click_delivery()
        displayed_delivery_info = best_sellers_page.displayed_delivery_info()
        assert displayed_delivery_info

    WORDS = [
        'blouse',
        '',
        'T-shirts',
        'dress'
    ]  # the Bug for the searching with word="dress". There is a "Blouse" and "T-shirt" in the result of the searching.

    @pytest.mark.parametrize("word", WORDS)
    def test_search_field(self, driver, word):
        """check out a search field with a necessary value"""
        best_sellers_page = BestSellers(driver)
        best_sellers_page.open_page()
        best_sellers_page.insert_text_in_search_field(word)  # insert a necessary word
        best_sellers_page.click_search_loupe()
        items_list = best_sellers_page.find_internal_text()  # the items name list after searching
        if word == '':
            assert 'Please enter a search keyword' in best_sellers_page.check_alert_block_text()
            print('color', best_sellers_page.check_alert_block_color())
            rgba = best_sellers_page.check_alert_block_color()  # rgba format in tuple is a format of alert block color
            r, g, b, alpha = ast.literal_eval(rgba.strip("rgba"))
            hex_value = '#%02x%02x%02x' % (r, g, b)  # convert rgb to hex format color
            assert hex_value == '#fe9126', 'Invalid color of alert block'  # right color is orange(#fe9126)
        else:
            counter = 0
            for name in items_list:
                if word.lower() in name.lower():
                    counter += 1

            assert counter == len(items_list), f'The search result with word={word} is a wrong.'


class TestAboutUsPage:
    def test_three_parts(self, driver):
        """check out the titles of three site parts: OUR COMPANY, OUR TEAM and TESTIMONIALS"""
        about_us_page = AboutUs(driver)
        about_us_page.open_page()
        three_parts = about_us_page.find_text_in_elements()
        assert 'OUR COMPANY' and 'OUR TEAM' and 'TESTIMONIALS' in three_parts

    def test_go_to_home_page(self, driver):
        """check out the return to the home page via the house icon"""
        about_us_page = AboutUs(driver)
        about_us_page.open_page()
        about_us_page.click_house_icon()
        assert 'http://automationpractice.com/index.php' == about_us_page.find_current_url()

    def test_go_to_top_menu(self, driver):
        """check out the successful transition to menu point 'Top' in the pop-up menu: Women->Top"""
        about_us_page = AboutUs(driver)
        about_us_page.open_page()
        about_us_page.click_top_menu()
        assert 'http://automationpractice.com/index.php?id_category=4&controller=category' == \
               about_us_page.find_current_url()


class TestOurStoresPage:
    def test_empty_newsletters_field(self, driver):
        """check out newsletters field with an empty field"""
        our_stores_page = OurStores(driver)
        our_stores_page.open_page()
        our_stores_page.fill_email_in_newsletters_field(email='')
        our_stores_page.click_submit_button()
        home_page = HomePage(driver)
        assert 'Newsletter : Invalid email address.' in home_page.check_alert_block()

    def test_newsletters_field_with_registered_email(self, driver):
        """check out newsletters field with a registered email"""
        our_stores_page = OurStores(driver)
        our_stores_page.open_page()
        our_stores_page.fill_email_in_newsletters_field(email='mine@mail.com')
        our_stores_page.click_submit_button()
        home_page = HomePage(driver)
        assert 'Newsletter : This email address is already registered.' in home_page.check_alert_block()

    def test_newsletters_field_with_unregistered_email(self, driver):
        """check out newsletters field with an unregistered new email"""
        our_stores_page = OurStores(driver)
        our_stores_page.open_page()
        our_stores_page.fill_email_in_newsletters_field(email='czxcvcxbv45@mail.com')
        our_stores_page.click_submit_button()
        home_page = HomePage(driver)
        assert 'Newsletter : You have successfully subscribed to this newsletter.' in home_page.check_alert_block()

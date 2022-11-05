from page.home_page import HomePage
from page.about_page import AboutUsPage

# Test page 3 http://automationpractice.com/index.php?id_cms=4&controller=cms
def test_dresses_button_is_present(driver):
    home_page = HomePage(driver)
    home_page.open_page() # open page http://automationpractice.com/
    home_page.click_about_us_button()
    about_page = AboutUsPage(driver)
    assert about_page.dresses_button()
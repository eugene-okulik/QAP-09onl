from pages.about_us_page import AboutUsPage


def test_our_stores(chrome_driver):
    about_us = AboutUsPage(chrome_driver)
    about_us.open_about_us_page()
    assert about_us.check_about_us_text()
    print(about_us.check_about_us_text())
    assert about_us.check_our_company_text()
    print(about_us.check_our_company_text())
    assert about_us.check_our_team_text()
    print(about_us.check_our_team_text())

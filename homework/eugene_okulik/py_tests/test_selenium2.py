import pytest
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert

@pytest.mark.skip
@pytest.mark.parametrize(
    'product_id',
    [1, 2, 3]
)
def test_add_to_cart(driver, product_id, hello):
    print(hello)
    driver.get('https://demoblaze.com/')
    product_link = driver.find_element(By.CSS_SELECTOR, f'a[href="prod.html?idp_={product_id}"]')
    product_link.click()
    button = driver.find_element(By.CSS_SELECTOR, f'a[onclick="addToCart({product_id})"]')
    assert button.is_displayed()


@pytest.mark.skip
def test_iframe(driver):
    driver.get('http://automationpractice.com/index.php')
    eye = driver.find_element(By.CLASS_NAME, 'icon-eye-open')
    eye.click()
    sleep(15)  # Demo
    i_frame = driver.find_element(By.CSS_SELECTOR, 'iframe[class="fancybox-iframe"]')
    driver.switch_to.frame(i_frame)
    print(driver.find_element(By.CSS_SELECTOR, 'h1[itemprop="name"]').text)
    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()
    driver.switch_to.default_content()
    x_button = driver.find_element(By.CSS_SELECTOR, 'a[class="fancybox-item fancybox-close"]')
    x_button.click()
    sleep(3)  # Demo


@pytest.mark.skip
def test_menu(driver):
    driver.get('http://automationpractice.com/index.php')
    women = driver.find_element(By.CSS_SELECTOR, 'a[title="Women"]')
    blouses = driver.find_element(By.CSS_SELECTOR, 'a[title="Blouses"]')
    ActionChains(driver).move_to_element(women).click(blouses).perform()
    sleep(5)  # Demo


def test_drag(driver):
    driver.get('https://demoqa.com/droppable')
    one = driver.find_element(By.ID, 'draggable')
    two = driver.find_element(By.ID, 'droppable')
    ActionChains(driver).drag_and_drop(one, two).perform()
    assert 'Dropped!' in two.text
    sleep(3)


def test_alert(driver):
    sleep(3)
    driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    first_button = driver.find_element(By.ID, 'alertexamples')
    second_button = driver.find_element(By.ID, 'confirmexample')
    third_button = driver.find_element(By.ID, 'promptexample')
    second_button.click()
    sleep(2)
    print(Alert(driver).text)
    Alert(driver).accept()
    driver.save_screenshot('file.png')
    # confirm = driver.find_element(By.ID, 'confirmreturn').text
    # assert confirm == 'false'
    sleep(3)

import pytest

from selenium.webdriver.common.by import By
from time import sleep


TEST_DATA = [5, 9, 4, 8]

@pytest.mark.skip
@pytest.mark.parametrize(
    'numb',
    TEST_DATA
)
def test_aa1(numb):
    print('test aa1')
    assert numb == 9


def test_aa2(tmp_path):
    d = tmp_path
    # d.mkdir()
    with open(f'{d}/file.txt', 'w') as text_file:
        text_file.write('lkasdfkjhaslkdjfhasd')
    print('test aa2')
    assert 2 == 2


def test_nava(driver):
    print('testing nava')
    driver.get('https://demoblaze.com/')
    element = driver.find_element(By.ID, 'nava')
    assert element.is_displayed()


@pytest.mark.skip
def test_signin2(driver):
    print('testing signin2')
    driver.get('https://demoblaze.com/')
    element = driver.find_element(By.ID, 'signin2')
    assert element.is_displayed()

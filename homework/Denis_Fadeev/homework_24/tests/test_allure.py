import allure
import pytest

checking_text = 'qwerty'


@pytest.fixture(scope='session')
def tests():
    print('Before tests')
    yield None
    print('After tests')


@pytest.fixture(scope='function')
def test():
    print('Before test')
    yield None
    print('After test')


@allure.feature('Simple test with numbers')
@allure.story('Addition of prime numbers')
def test_number_1(tests, test):
    print(f'==|Test_1|')
    with allure.step('variable one'):
        a = 50
    with allure.step('variable two'):
        b = 50
    with allure.step('Compare values'):
        assert a + b == 100


@allure.feature('Simple test with numbers')
@allure.story('Prime Number Comparison')
def test_number_2(test):
    print(f'==|Test_2|')
    assert 2 == 2


@allure.feature('Simple test with text')
@allure.story('Text comparison')
def test_number_1_text(test):
    print(f'==|Test_1_TEXT|')
    assert 'qwerty' == checking_text


@allure.feature('Simple test with text')
@allure.story('Addition of text')
def test_number_2_text(test):
    print(f'==|Test_2_TEXT|')
    assert 'qwe' + 'rty' == checking_text


@allure.feature('Skip test')
@pytest.mark.skip('Unnecessary test')
def test_number_3(test):
    print(f'==|Test_10|')
    assert 10 == 10
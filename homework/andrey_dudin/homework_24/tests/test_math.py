import allure
import pytest

result_number = 4
result_text = "text"
TEST_DATA = [(2,2),(3,3),(4,4)]


@pytest.fixture(scope='session')
def session_scope():
    print("Before session")
    yield print("Print in yield session scope")
    print("After session")


@pytest.fixture(scope="function")
def func_scope():
    print("Before function")
    yield print("Print in yield function scope")
    print("After function")


@allure.story('Проверка арифметических операций над числами')
@allure.feature('Умножение')
def test_one(session_scope, func_scope):
    with allure.step('присваиваем значение первой переменной'):
        a1 = 2
    with allure.step ('Присваиваем значение второй переменной'):
        a2 = 2
    with allure.step('Сравниваем значения'):
        assert a1 * a2 == result_number

@allure.story('Проверка арифметических операций над числами')
@allure.feature('Равенство')
def test_two(func_scope):
    assert 4 == result_number

@allure.story('Проверка арифметических операций над текстом')
@allure.feature('Конкатенация')
def test_three(func_scope):
    assert "te" + "xt" == result_text

@allure.story('Проверка арифметических операций над числами')
@allure.feature('Сложение')
def test_four(func_scope):
    assert 2+1+1 == result_number

@allure.story('Проверка арифметических операций над числами')
@allure.feature('Равенство')
@pytest.mark.skip("Failed test. Don't run this test")
def test_five(func_scope):
    assert 5 == result_number

@allure.story('Проверка арифметических операций над числами')
@allure.feature('Сложение')
def test_six(func_scope):
    assert 1+1 == 2

@allure.story('Проверка арифметических операций над текстом')
@allure.feature('Текстовое равенство')
def test_seven(func_scope):
    assert "text" == result_text

@allure.story('Проверка арифметических операций над числами')
@allure.feature('Умножение')
def test_eight(func_scope):
    assert 1 * 1 == 1

@allure.story('Проверка арифметических операций над числами')
@allure.feature('Числовое равенство')
def test_nine():
    assert 10 == 10


@allure.story('Проверка арифметических операций над числами')
@allure.feature('Параметрический тест')
@pytest.mark.parametrize("value1, value2",  TEST_DATA)
def test_ten(func_scope, value1, value2):
    assert value1 == value2
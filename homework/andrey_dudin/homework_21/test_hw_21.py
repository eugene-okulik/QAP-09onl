'''
Создайте 10 тестов, которые проверяют сами себя (бессмысленные тесты, которые я показывал на занятии, типа assert 2+2 == 4)
Добавьте действие, которое отрабатывает перед всем запуском тестов, а также после окончания тестирования.
Действие какое-нибудь простое. Например, пусть часть,которая отрабатывает до делает print('before'),
а часть, которая отрабатывает после делает print('after')
Добавьте действие, которое отрабатывает до и после каждого теста
Сделайте возможным запуск тестов помеченных как “simple” и “hard”
Пропустите выполнение одного теста и пометьте причину пропуска
Хотя бы один тест должен работать с набором тестовых данных (этот про parametrize, если выполните все задание
до 17-го октября, то этот пункт - необязательный)
Все тесты должны запускаться с помощью команды pytest.
'''

import pytest

result_number = 4
result_text = "text"

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


@pytest.mark.simple
def test_one(session_scope, func_scope):
    assert 2 * 2 == result_number


def test_two(func_scope):
    assert 4 == result_number


def test_three(func_scope):
    assert "te" + "xt" == result_text


def test_four(func_scope):
    assert 2+1+1 == result_number


@pytest.mark.skip("Failed test. Don't run this test")
def test_five(func_scope):
    assert 5 == result_number


def test_six(func_scope):
    assert 1+1 == 2


def test_seven(func_scope):
    assert "text" == result_text


def test_eight(func_scope):
    assert 1 * 1 == 1

#Test without func_scope fixture
def test_nine():
    assert 10 == 10


TEST_DATA = [(2,2),(3,3),(4,4)]

@pytest.mark.parametrize("value1, value2",  TEST_DATA)
@pytest.mark.hard
def test_ten(func_scope, value1, value2):
    assert value1 == value2
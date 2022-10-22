# Создайте 10 тестов, которые проверяют сами себя (бессмысленные тесты, которые я показывал на занятии,
# типа assert 2+2 == 4)
# Добавьте действие, которое отрабатывает перед всем запуском тестов, а также после окончания тестирования.
# Действие какое-нибудь простое. Например, пусть часть,которая отрабатывает до делает print('before'), а часть,
# которая отрабатывает после делает print('after')
# Добавьте действие, которое отрабатывает до и после каждого теста
# Сделайте возможным запуск тестов помеченных как “simple” и “hard”
# Пропустите выполнение одного теста и пометьте причину пропуска
# Хотя бы один тест должен работать с набором тестовых данных (этот про parametrize, если выполните все задание
# до 17-го октября, то этот пункт - необязательный)

import pytest
from datetime import datetime


@pytest.fixture(scope='session')    # this fixture will launch before all tests and end after all tests
# @pytest.fixture(scope='function')    # this fixture will launch before each test and end after each test
def fixture_practise():
    print('\nThe beginning of the testing')
    yield None
    print('\nEnd of the testing')


@pytest.fixture(scope='function')
def all_tests():
    print('\nHi! The test begins')
    yield None
    print('\nBye! The test is over')


@pytest.mark.simple
def test_one(fixture_practise, all_tests):
    print('Testing the first function')
    assert 5 == 5


@pytest.mark.skipif(datetime.now().year == 2022, reason='not supported in this year')
@pytest.mark.simple
def test_two(fixture_practise, all_tests):
    print('Testing the second function')
    assert 10 / 2 == 5


@pytest.mark.parametrize(
    'value',
    [6, 12, 20, 46]
)
@pytest.mark.simple
def test_three(fixture_practise, value, all_tests):
    print('Testing the third function')
    assert 4 % 2 == 0


@pytest.mark.hard
def test_four(fixture_practise, all_tests):
    print('Testing the fourth function')
    assert (1 + 1) ** (5 - 2) == 8


@pytest.mark.simple
def test_five(fixture_practise, all_tests):
    print('Testing the fifth function')
    assert 5 ** 2 == 25


@pytest.mark.simple
def test_six(fixture_practise, all_tests):
    print('Testing the sixth function')
    assert 9 // 2 == 4


@pytest.mark.simple
def test_seven(fixture_practise, all_tests):
    print('Testing the seventh function')
    assert 1 == 1


@pytest.mark.simple
def test_eight(fixture_practise, all_tests):
    print('Testing the eighth function')
    assert 10 - 3 == 7


@pytest.mark.hard
def test_nine(fixture_practise, all_tests):
    print('Testing the ninth function')
    assert 2 + 2 * 2 == 6


@pytest.mark.skip('the feature has not been supported on the project yet')
@pytest.mark.simple
def test_ten(fixture_practise, all_tests):
    print('Testing the tenth function')
    assert 2 != 3


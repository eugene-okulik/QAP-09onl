# Pytest
# 1. Создайте 10 тестов, которые проверяют сами себя
#       (бессмысленные тесты, которые я показывал на занятии, типа assert 2+2 == 4) +
# 2.Добавьте действие, которое отрабатывает перед всем запуском тестов, а также после окончания тестирования.
#       Действие какое-нибудь простое. Например, пусть часть, которая отрабатывает до делает print('before'),
#       а часть, которая отрабатывает после делает print('after') +
# 3. Добавьте действие, которое отрабатывает до и после каждого теста +
# 4. Сделайте возможным запуск тестов помеченных как “simple” и “hard” +
# 5. Пропустите выполнение одного теста и пометьте причину пропуска +
# 6. Хотя бы один тест должен работать с набором тестовых данных +
#       (этот про parametrize, если выполните все задание до 17-го октября, то этот пункт - необязательный)
#
# Все тесты должны запускаться с помощью команды pytest.

import pytest


@pytest.fixture(scope='session')
def testing_session():
    print(f'{"̅" * 20} BEFORE ALL TEST {"̅" * 20}')
    yield None
    print(f'{"̅" * 20} AFTER ALL TEST {"̅" * 20}')


@pytest.fixture(scope='function')
def one_test():
    print(f'{"̅" * 20} BEFORE EACH TEST {"̅" * 20}')
    yield None
    print(f'{"̅" * 20} AFTER EACH TEST {"̅" * 20}')


@pytest.mark.hard
def test_one(testing_session, one_test):
    print('<Test One>:')
    assert 1 == 1


@pytest.mark.simple
def test_two(one_test):
    print('<Test Two>:')
    assert 2 == 2


@pytest.mark.skip('Reason: Number of test THREE')
def test_three(one_test):
    print('<Test Three>:')
    assert 3 == 3


TEST_DATA = [4, 4.0, 3, 5]


@pytest.mark.parametrize(
    'num',
    TEST_DATA
)
def test_four(one_test, num):
    print('<Test Four>:')
    assert num == 4


@pytest.mark.simple
def test_five(one_test):
    print('<Test Five>:')
    assert 5 == 5


def test_six(one_test):
    print('<Test Six>:')
    assert 6 == 6


def test_seven(one_test):
    print('<Test Seven>:')
    assert 7 == 7


def test_eight(one_test):
    print('<Test Eight>:')
    assert 8 == 8


@pytest.mark.simple
def test_nine(one_test):
    print('<Test Nine>:')
    assert 9 == 9


@pytest.mark.hard
def test_ten(one_test):
    print('<Test Ten>:')
    assert 10 == 10

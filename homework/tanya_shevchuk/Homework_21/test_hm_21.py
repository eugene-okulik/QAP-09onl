# Pytest
# 1.  Создайте 10 тестов, которые проверяют сами себя (бессмысленные тесты, которые я показывал на занятии, типа assert 2+2 == 4)
# 2. Добавьте действие, которое отрабатывает перед всем запуском тестов, а также после окончания тестирования. Действие
# какое-нибудь простое. Например, пусть часть,которая отрабатывает до делает print('before'), а часть, которая
# отрабатывает после делает print('after')
# 3. Добавьте действие, которое отрабатывает до и после каждого теста
# 4. Сделайте возможным запуск тестов помеченных как “simple” и “hard”
# 5. Пропустите выполнение одного теста и пометьте причину пропуска
# Все тесты должны запускаться с помощью команды pytest.

import pytest


@pytest.fixture(scope='session')
def session_scope():
    print('Before all tests')
    yield None
    print('after all tests')


@pytest.fixture(scope="function")
def funct_scope():
    print('Before this test')
    yield None
    print('after this test')


@pytest.mark.hard
def test_1_hard(session_scope, funct_scope):
    print("test one")
    assert 1 == 1


@pytest.mark.simple
def test_2_simple(funct_scope):
    print("test 2")
    assert 2 == 2


@pytest.mark.skip("Not February now:)")
def test_3(funct_scope):
    print("test 3")
    assert 3 == 3


def test_4(funct_scope):
    print("test 4")
    assert 4 == 4


def test_5(funct_scope):
    print("test 5")
    assert 5 == 5


def test_6(funct_scope):
    print("test 6")
    assert 6 == 6


def test_7(funct_scope):
    print("test 7")
    assert 7 == 7


def test_8(funct_scope):
    print("test 8")
    assert 8 == 8


def test_9(funct_scope):
    print("test 9")
    assert 9 == 9


def test_10(funct_scope):
    print("test ten")
    assert 10 == 10

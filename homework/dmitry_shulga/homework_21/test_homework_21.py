import pytest


@pytest.fixture(scope='session')
def all_tests():
    print('\nBefore')
    yield None
    print('\nAfter')


@pytest.fixture(scope='function')
def each_test():
    print('\nReady')
    yield None
    print('\nDone')


def summ(n):
    return n+n


@pytest.mark.hard
def test_sum(all_tests, each_test):
    print("Testing sum")
    assert 4 == summ(2)


def multi(n):
    return n*n


@pytest.mark.hard
def test_multi(all_tests, each_test):
    print("Testing multi")
    assert 9 == multi(3)


def division(n):
    return n/n


@pytest.mark.hard
def test_division(all_tests, each_test):
    print("Testing division")
    assert 1 == division(1)


def subtraction(n):
    return n-n


@pytest.mark.hard
def test_subtraction(all_tests, each_test):
    print("Testing subtraction")
    assert 0 == subtraction(1)


TEST_DATA = [1, 2, 3]


@pytest.mark.parametrize("num", TEST_DATA)
@pytest.mark.simple
def test_number1(all_tests, each_test, num):
    assert num == num


@pytest.mark.simple
def test_number2(all_tests, each_test):
    assert 2 == 2


@pytest.mark.simple
def test_number3(all_tests, each_test):
    assert 3 == 3


@pytest.mark.simple
def test_number4(all_tests, each_test):
    assert 4 == 4


@pytest.mark.simple
def test_number5(all_tests, each_test):
    assert 5 == 5


@pytest.mark.skip("Feature not implemented")
def test_number6(all_tests, each_test):
    assert 6 == 6





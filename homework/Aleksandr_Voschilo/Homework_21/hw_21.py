import pytest


@pytest.fixture(scope='session')
def all_tests():
    print('\nBefore all tests')
    yield None
    print('\nAfter all tests')


@pytest.fixture(scope='function')
def each_test():
    print('\nBefore test')
    yield None
    print('\nAfter test')


@pytest.mark.simple
def test_1(all_tests, each_test):
    assert 1 == 1


@pytest.mark.simple
def test_2(each_test):
    assert 2 == 2


@pytest.mark.simple
def test_3(each_test):
    assert 3 == 3


@pytest.mark.hard
def test_4(each_test):
    assert 4 == 4


@pytest.mark.hard
def test_5(each_test):
    assert 5 == 5


@pytest.mark.hard
def test_6(each_test):
    assert 6 == 6


@pytest.mark.skip('feature not implemented')
def test_7(each_test):
    assert 7 == 7


TEST_DATA = [7, 8, 9]


@pytest.mark.parametrize(
    'num',
    TEST_DATA
)
def test_8(each_test, num):
    assert num == 8


def test_9(each_test):
    assert 9 == 9


def test_10(each_test):
    assert 10 == 10

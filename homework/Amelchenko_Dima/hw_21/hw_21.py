import pytest

#pytest -v -s homework\Amelchenko_Dima\hw_21\hw_21.py
#pytest -v -s -m "hard or simple"  homework\Amelchenko_Dima\hw_21\hw_21.py

TEST_DATA = [2, 3, 4]


@pytest.fixture(scope='session')
def all_tests():
    print('///////////////////Befor///////////////////')
    yield None
    print('///////////////////After///////////////////')


@pytest.fixture(scope='function')
def every_tests():
    print('Befor test', end=' ')
    yield None
    print(' After test')

@pytest.mark.simple
def test_one(all_tests, every_tests):
    assert 1 + 0 == 1


@pytest.mark.hard
def test_two(every_tests):
    assert 1 + 1 == 2


@pytest.mark.simple
def test_three(every_tests):
    assert 2 + 1 == 3


def test_four(every_tests):
    assert 2 + 2 == 4


def test_five(every_tests):
    assert 2 + 3 == 5


def test_six(every_tests):
    assert 3 + 3 == 6


def test_seven(every_tests):
    assert 4 + 3 == 7


def test_eight(every_tests):
    assert 2 + 2 + 4 == 8


@pytest.mark.skip("test doesn't work")
def test_nine(every_tests):
    assert 3 + 3 + 3 == 12


@pytest.mark.parametrize(
    'arg',
    TEST_DATA
)
def test_ten(every_tests, arg):
    assert arg == arg
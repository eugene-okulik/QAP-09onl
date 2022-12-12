import pytest


@pytest.fixture(scope='session')
def session_scope():
    print("Start")
    yield None
    print("Finish")


@pytest.fixture(scope="function")
def func_scope():
    print("Before func")
    yield None
    print("After func")


@pytest.mark.simple
def test_one(session_scope, func_scope):
    assert 1 * 2 == 2


def test_two(func_scope):
    assert 10 / 5 == 2


def test_three(func_scope):
    assert 5 + 5 == 10


def test_four(func_scope):
    assert 5 + 5 + 10 == 20


@pytest.mark.skip("This fucn will be tested late")
def test_five(func_scope):
    assert 10 * 10 == 100


def test_six(func_scope):
    assert 25 - 5 == 20


def test_seven(func_scope):
    assert 10 + 2 + 3 == 15


def test_eight(func_scope):
    assert 80 * 10 == 800


def test_nine(func_scope):
    assert 10 * 10 * 10 == 1000


TEST_DATA = [10, 20, 30]


@pytest.mark.parametrize("number1", TEST_DATA)
@pytest.mark.hard
def test_ten(func_scope, number1):
    assert number1 * number1 == number1 * number1

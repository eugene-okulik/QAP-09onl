import pytest

@pytest.fixture(scope="function")
def func_scope():
    print("Before func")
    yield None
    print("After func")

@pytest.fixture(scope='session')
def session_scope():
    print("Start")
    yield None
    print("Finish")

@pytest.mark.simple
def test_1(func_scope):
    assert 12 / 4 == 3

def test_2(func_scope):
    assert 1 + 4 + 8 == 13

def test_3(func_scope, session_scope):
    assert 1 * 2 == 2

def test_4(func_scope):
    assert 3 + 7 == 10


@pytest.mark.skip("Будет запущен позже")
def test_5(func_scope):
    assert 7 + 2 + 3 == 12

def test_6(func_scope):
    assert 5 * 10 == 50

def test_7(func_scope):
    assert 32 - 8 == 24

def test_8(func_scope):
    assert 35 * 10 == 350

def test_9(func_scope):
    assert 5 * 5 * 5 == 125


Test = [10, 20, 30]


@pytest.mark.parametrize("number3", Test)
@pytest.mark.hard
def test_10(func_scope, number3):
    assert number3 * number3 == number3 * number3

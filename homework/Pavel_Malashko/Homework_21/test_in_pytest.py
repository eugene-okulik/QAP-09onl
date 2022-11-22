import pytest


@pytest.fixture(scope="session")
def all_function_testing():
    print("Before testing all functions")
    yield None
    print("\nAfter testing all functions")


@pytest.fixture(scope='function')
def single_function_testing():
    print("Before testing function")
    yield None
    print("\nAfter testing function")


def test_1(all_function_testing, single_function_testing):
    assert 1 == 1


def test_2(all_function_testing, single_function_testing):
    assert 2 == 2


@pytest.mark.skip('#bug15402')
def test_3(all_function_testing, single_function_testing):
    assert 3 == 3


def test_4(all_function_testing, single_function_testing):
    assert 4 == 4


@pytest.mark.simple
def test_5(all_function_testing, single_function_testing):
    assert 5 == 5


@pytest.mark.hard
def test_6(all_function_testing, single_function_testing):
    assert 6 == 6


def test_7(all_function_testing, single_function_testing):
    assert 7 == 7


@pytest.mark.parametrize("number, expected", [("8", 8)])
def test_8(all_function_testing, single_function_testing, number, expected):
    assert eval(number) == expected


def test_9(all_function_testing, single_function_testing):
    assert 9 == 9


def test_10(all_function_testing, single_function_testing):
    assert 10 == 10

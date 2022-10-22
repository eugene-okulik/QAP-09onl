import pytest


@pytest.fixture(scope='session')
def testing():
    print(f"\n{'-' * 45}Start testing{'-' * 45}")
    yield None
    print(f"\n{'-' * 45}Finish testing{'-' * 45}")


@pytest.fixture(scope='function')
def all_tests():
    print(f"\n{'-' * 20}Ready{'-' * 20}")
    yield None
    print(f"\n{'-' * 20}Done{'-' * 20}")


@pytest.mark.simple
def test_number1(testing, all_tests):
    assert 1 == 1


@pytest.mark.simple
def test_number2(testing, all_tests):
    assert 2 == 2


@pytest.mark.simple
def test_number3(testing, all_tests):
    assert 3 == 3


@pytest.mark.simple
def test_number4(testing, all_tests):
    assert 4 == 4


@pytest.mark.simple
def test_number5(testing, all_tests):
    assert 5 == 5


TEST_DATA = [3, 5, 7]


@pytest.mark.parametrize('num', TEST_DATA)
@pytest.mark.hard
def test_number6(testing, all_tests, num):
    assert num >= 6


@pytest.mark.skip('I so wanted')
@pytest.mark.hard
def test_number7(testing, all_tests):
    assert 7 == 7


@pytest.mark.hard
def test_number8(testing, all_tests):
    assert 8 == 8


@pytest.mark.hard
def test_number9(testing, all_tests):
    assert 9 == 9


@pytest.mark.hard
def test_number10(testing, all_tests):
    assert 10 == 10

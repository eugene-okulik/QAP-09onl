import pytest

TEST_DATA = [2, 3, 4]


@pytest.fixture(scope='session')
def tests():
    print('Before tests')
    yield None
    print('After tests')


@pytest.fixture(scope='function')
def test():
    print('Before test')
    yield None
    print('After test')


@pytest.mark.simple
def test_number_1(tests, test):
    print(f'==|Test_1|')
    assert 1 == 1


@pytest.mark.hard
def test_number_2(test):
    print(f'==|Test_2|')
    assert 2 == 2


@pytest.mark.simple
def test_number_3(test):
    print(f'==|Test_3|')
    assert 3 == 3


@pytest.mark.hard
def test_number_4(test):
    print(f'==|Test_4|')
    assert 4 == 4


@pytest.mark.parametrize(
    'num',
    TEST_DATA
)
@pytest.mark.simple
def test_number_5(test, num):
    print(f'==|Test_5|')
    assert 3 == 3


@pytest.mark.hard
def test_number_6(test):
    print(f'==|Test_6|')
    assert 6 == 6


@pytest.mark.simple
def test_number_7(test):
    print(f'==|Test_7|')
    assert 7 == 7


@pytest.mark.hard
def test_number_8(test):
    print(f'==|Test_8|')
    assert 8 == 8


@pytest.mark.simple
def test_number_9(test):
    print(f'==|Test_9|')
    assert 9 == 9


@pytest.mark.skip('Unnecessary test')
def test_number_10(test):
    print(f'==|Test_10|')
    assert 10 == 10

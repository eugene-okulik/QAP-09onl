import pytest


@pytest.fixture(scope='session')
def testing():
    print(f'{"-" * 5} Before all test! {"-" * 5}')
    yield None
    print(f'{"-" * 5} After all test! {"-" * 5}')


@pytest.fixture(scope='function')
def test_one():
    print(f'{"-" * 5} Before test! {"-" * 5}')
    yield None
    print(f'{"-" * 5} After test! {"-" * 5}')


@pytest.mark.simple
def test_simple_1(testing, test_one):
    print('testing_simple_1')
    assert 5 == 5


@pytest.mark.simple
def test_simple_2(test_one):
    print('testing_simple_2')
    assert 6 == 6


@pytest.mark.hard
def test_hard_1(test_one):
    print('testing_hard_1')
    assert 1 == 1


@pytest.mark.hard
def test_hard_2(test_one):
    print('testing_hard_2')
    assert 2 == 2


@pytest.mark.skip('This test not working')
def test_skip(test_one):
    print('testing_skip')
    assert 3 == 3


TEST_DATA = [2, 3, 4]


@pytest.mark.parametrize(
    'num',
    TEST_DATA
)


class TestingParametrize:
    def test_one(self, num):
        assert num == 2

    def test_two(self, num):
        assert num == 3

    def test_three(self, num):
        assert num == num
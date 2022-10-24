import pytest


@pytest.fixture(scope='session')
def all_testing_session():
    print('\nBEFORE: HELLO I am a BLOCK BEFORE ALL TEST RUN')

    yield None
    print('\nAFTER: BYE, ALL TESTS ARE FINISHED NOW.')


@pytest.fixture(scope='function')
def single_test():
    print('\nI am ready to check only this test')
    yield None
    print('\nI am done with this test')


# @pytest.mark.skip
class TestCollection:
    @pytest.mark.simple
    def test_one(self, single_test, all_testing_session):
        print('The first test ', end='')
        assert 1 == 1

    # @pytest.mark.skip
    def test_two(self, single_test):
        print('The second test ', end='')
        assert 2 == 2

    @pytest.mark.hard
    def test_three(self, single_test):
        print('The third test ', end='')
        assert 3 == 3

    # @pytest.mark.skip
    def test_four(self, single_test):
        print('The fourth test ', end='')
        assert 4 == 4

    # @pytest.mark.skip
    def test_five(self, single_test):
        print('The fifth test ', end='')
        assert 5 == 5

    # @pytest.mark.skip
    def test_six(self, single_test):
        print('The sixth test ', end='')
        assert 6 == 6

    @pytest.mark.simple
    def test_seven(self, single_test):
        print('The seventh test ', end='')
        assert 7 == 7

    @pytest.mark.parametrize('num', [10, 8, 90, 100])
    def test_eight(self, num, single_test):
        print(f'The eighth test for value {num} ', end='')
        assert 100 - num >= 10

    @pytest.mark.skip('The bug#1022a')
    # @pytest.mark.skipif(datetime.now().month == 10, 'not supported in this month')
    # @pytest.mark.skipif(system == Windows, 'not supported in this month')
    def test_nine(self, single_test):
        print('The ninth test ', end='')
        assert 9 == 9

    @pytest.mark.hard
    def test_ten(self, single_test):
        print('The tenth test ', end='')
        assert 10 == 10

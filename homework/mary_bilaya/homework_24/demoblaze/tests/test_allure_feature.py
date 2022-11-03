import allure
import pytest


@allure.feature('Testing allure features')
class TestAllure:

    @allure.title('simple function')
    @allure.description('test 1')
    @allure.story('practise')
    @allure.step('step number 1')
    @allure.issue('https://demoblaze.com/', name='click to go on testing page')
    def test_n1(self):
        assert 2 == (1 + 1)

    @allure.title('simple function')
    @allure.description('test 2')
    @allure.story('practise')
    @allure.step('step number 2')
    @allure.testcase('https://demoblaze.com/cart.html#', name='click to go on cart page')
    def test_n2(self):
        assert 5 != 2

    @allure.title('print function')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('test 3')
    @allure.story('work')
    @allure.step('step number 3')
    def test_n3(self, name='Mary', age=33):
        print(f'My name is {name}. I am {age} years old')

    @allure.title('logical function')
    @allure.description('test 4')
    @allure.story('practise')
    @allure.step('step number 4')
    def test_n4(self):
        assert 2 + 3 * 2 == 8

    @allure.title('parametrize function')
    @allure.description('test 5')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story('work')
    @allure.step('step number 5')
    @pytest.mark.parametrize(
        'value',
        [12, 4, 34, 6]
    )
    def test_n5(self, value):
        assert value % 2 == 0

    @allure.title('simple function')
    @allure.description('test 6')
    @allure.story('work')
    @allure.step('step number 6')
    def test_n6(self):
        assert 9 // 2 == 4

    @allure.title('hard function')
    @allure.description('test 7')
    @allure.story('practise')
    @allure.step('step number 7')
    def test_n7(self):
        assert 3 ** 3 == 27




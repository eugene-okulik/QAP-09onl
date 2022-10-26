import allure


@allure.feature('Authentication')
@allure.story('registration')
def test_n1():
    assert 1 == 1


@allure.feature('Authentication')
@allure.story('registration')
def test_n2():
    assert 2 == 2


@allure.feature('Authentication')
@allure.story('login')
def test_n3():
    assert 3 == 3


@allure.feature('Authentication')
@allure.story('login')
def test_n4():
    assert 4 == 4


@allure.feature('Cart')
@allure.story('checkout')
def test_n5():
    assert 6 == 6

import pytest


def cube(n):
    return n * n * n


def test_cube():
    print('Testing the cube', end=' ')
    assert 8 == cube(3)


def test_number1():
    assert 1 == 1

import unittest
import pytest


def square(n: int):
    return n * n


def cub(n: int):
    return n * n * n


class TestSimpleCases(unittest.TestCase):

    def test_square(self):
        print('Testing the square')
        self.assertEqual(4, square(2))

    def test_cube(self):
        print('Testing the cube')
        self.assertEqual(8, cub(2))
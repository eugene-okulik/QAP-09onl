import unittest
import my_code
from datetime import datetime


class TestSimpleCases(unittest.TestCase):

    def setUp(self):
        # set up crome driver
        print('Set up function')

    def tearDown(self):
        # driver.close()
        print('Tear down function')

    # @unittest.skipUnless(datetime.now().year == 2021, 'Not supported in this year')
    def test_square(self):
        print('Testing the square')
        self.assertEqual(4, my_code.square(2))

    # @unittest.skip('Bug #12312')
    def test_cube(self):
        print('Tesing the cube')
        self.assertEqual(8, my_code.cube(3))

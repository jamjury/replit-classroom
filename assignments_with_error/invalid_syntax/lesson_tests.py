import unittest
from main import example
from main import *
import math

class AssignmentWithValidTests(unittest.TestCase):
def setUp(self):
        print('oh no, a syntax error')

    def tearDown(self):
        print('teardown code here')

    def test_this_is_the_first_test(self):
        print('print')
        print('print')
        print('print')

    def test_this_is_the_second_test(self):
        print('more')

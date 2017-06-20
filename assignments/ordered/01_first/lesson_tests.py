import unittest
from main import example

print('this code falls into the intialization section')
intialization_section = 'right here'

class Hmmm():
    def __init__(self):
        print('here\'s where it gets a bit tricky')
        print('this should also be in init')

hmmm = Hmmm()

class AssignmentWithValidTests(unittest.TestCase):
    def setUp(self):
        print('setup code here')

    def tearDown(self):
        print('teardown code here')

    def test_this_is_the_first_test(self):
        print('print')
        print('print')
        print('print')

    def test_this_is_the_second_test(self):
        print('more')


print('this also falls into intialization')

class AssignmentWithValidTestsPart2(unittest.TestCase):
    def test_this_is_the_third_test(self):
        print('in another section')

print('and so does this')

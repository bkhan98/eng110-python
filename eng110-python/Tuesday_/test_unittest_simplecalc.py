# unit test is in this format
from simple_calc import SimpleCalc

import unittest

class Calctests(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2,4), 6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2,4), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 4), 4)

    def test_divide(self):
        self.assertEqual(self.calc.m)

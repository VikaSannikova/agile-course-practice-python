import unittest

from fraction.model.fraction import Fraction


class TestFractionClass(unittest.TestCase):
    def test_can_create_str_from_fraction(self):
        frac = Fraction(p=3, q=4)
        self.assertEqual(str(frac), '3/4')
        
    def test_can_reduce_fraction(self):
        frac = Fraction(p=5, q=10)
        self.assertTrue(frac.is_equal(1, 2))

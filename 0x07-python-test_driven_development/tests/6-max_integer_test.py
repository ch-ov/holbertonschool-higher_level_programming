#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
	""" Edge cases """
	def test_max(self):
		self.assertAlmostEqual(max_integer([-606]), -606)
		self.assertAlmostEqual(max_integer([11,12,13,14]), 14)
		self.assertAlmostEqual(max_integer([68,24,378,6989]), 6989)
		self.assertAlmostEqual(max_integer([-22,-78,-35,-75]), -22)
		self.assertAlmostEqual(max_integer([8,2,-3,5,1]), 8)
		self.assertAlmostEqual(max_integer([767,4667,23,547,54]), 4667)
		self.assertAlmostEqual(max_integer([111]), 111)
		self.assertAlmostEqual(max_integer([]), None)
		self.assertAlmostEqual(max_integer(), None)
		self.assertAlmostEqual(max_integer(["a", "b", "c", "d", "e"]), "e")
		self.assertAlmostEqual(max_integer("abcdefgh"), "h")
	def test_raise(self):
		self.assertRaises(TypeError, max_integer, 2)
		

if __name__ == "__main__":
    unittest.main()

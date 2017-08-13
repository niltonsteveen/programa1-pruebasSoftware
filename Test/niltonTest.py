import unittest

from Code.niltonCode import CodeDeviation

class TestsDeviation(unittest.TestCase):
	def testVacio(self):
		cd=CodeDeviation()
		deviation=cd.standardDeviation
		self.assertEqual(0,deviation)
if __name__ == '__main__':
	unittest.main()
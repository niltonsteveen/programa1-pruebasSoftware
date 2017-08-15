import unittest

from jorgeCode import Mean

class TestsMean(unittest.TestCase):
	meanObject= Mean()
	def testEmpty(self):
		array=[]		
		mean=self.meanObject.calculateMean(array)
		self.assertEqual(0, mean)
	def testNotNumbers(self):
		array=['fda', 43, 'saf'];
		mean=self.meanObject.calculateMean(array)
		self.assertEqual(0, mean)
if __name__ == '__main__':
	unittest.main()

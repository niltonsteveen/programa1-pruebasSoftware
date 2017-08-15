import unittest

from jorgeCode import Mean

class TestsMean(unittest.TestCase):
	
	def testEmpty(self):
		meanObject= Mean()
		self.assertEqual(0, meanObject.calculateMean([]))
	def testNotNumbers(self):
		meanObject1= Mean()
		self.assertEqual(0, meanObject1.calculateMean(['fda', 43, 'saf']))
	def testRealNumbers(self):
		meanObject2= Mean()
		self.assertNotEqual(2, meanObject2.calculateMean([1,1.7,3.8]))
	def testZeroDivision(self):
		meanObject3= Mean()
		self.assertEqual(0, meanObject3.calculateMean([]))
	
if __name__ == '__main__':
	unittest.main()

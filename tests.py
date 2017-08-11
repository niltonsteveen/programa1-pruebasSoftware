import unittest
class ejemploTest(unittest.TestCase):
	def runTest(self):
		numero1=2
		self.assertEqual(2,numero1)
if __name__ == '__main__':
    unittest.main()
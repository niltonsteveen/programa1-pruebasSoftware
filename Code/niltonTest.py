import unittest

from niltonCode import CodeDeviation

class TestsDeviation(unittest.TestCase):
	cd = CodeDeviation()
	def testVacio(self):
		deviation=self.cd.standardDeviation
		self.assertEqual(0,deviation)
	def testRaizNegativa(self):
		self.assertEqual(None,self.cd.calcularDesviacion(-1,2))
	def testUnSoloItem(self):
		self.assertEqual(None, self.cd.calcularDesviacion(5, 1))
	def testCalculoDesviacionConEntradasInvalidas(self):
		self.assertEqual(None, self.cd.calcularDesviacion('jhgkghlgl',3))

if __name__ == '__main__':
	unittest.main()
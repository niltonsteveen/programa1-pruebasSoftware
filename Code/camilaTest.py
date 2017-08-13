import unittest

from camilaCode import ReadFile

class TestsRead(unittest.TestCase):
    def setUp(self):
        self.read = ReadFile()
    def testReadFile(self):
        self.read.readFile("Code/numeros.txt")
        self.assertNotEqual(None, self.read.file)
    def testOnlyRead(self):
        self.read.readFile("Code/numeros.txt")
        self.assertTrue(self.read.onlyRead())
    def testReadNumbers():
        self.read.readFile("Code/numeros.txt")
        self.assertEqual([1,4,5,7,9],self.read.muestra)

if __name__ == '__main__':
    unittest.main()

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
    

if __name__ == '__main__':
    unittest.main()

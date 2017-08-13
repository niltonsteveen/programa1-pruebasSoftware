import unittest

from camilaCode import ReadFile

class TestsRead(unittest.TestCase):
    def setUp(self):
        self.read = ReadFile()
    def testReadFile():
        self.read.readFile("./numeros.txt")
        self.assertNotEqual(None, self.read.file)
    def testOnlyRead():
        self.assertTrue(self.read.onlyRead())
    

if __name__ == '__main__':
    unittest.main()

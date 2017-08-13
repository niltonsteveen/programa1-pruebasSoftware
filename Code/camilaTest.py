import unittest

from camilaCode import ReadFile

class TestsRead(unittest.TestCase):
    def setUp(self):
        self.read = ReadFile()
    def testLeerArchivo():
        self.assertEqual(True,self.read.onlyRead())

if __name__ == '__main__':
    unittest.main()

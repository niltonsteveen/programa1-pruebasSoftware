import unittest

from linkedList import LinkedList
from linkedList import Node
from linkedList import myExc

class TestNode(unittest.TestCase):
    def setUp(self):
        self.node = Node()
    def testCreateNode(self):
        self.node.createNode(3, None)
        self.assertEqual(3, self.node.data)
    def testChangeLink(self):
        node2 = Node()
        self.node.changeLink(node2)
        self.assertEqual(node2, self.node.link)

class TestsLinkedList(unittest.TestCase):
    def setUp(self):
        self.linkedList = LinkedList()
    def testCreateHeadNode(self):
        node = Node()
        node.createNode(0, None)
        self.linkedList.createLinkedList()
        self.assertEqual(node.data, self.linkedList.nodeHead.data)
        self.assertEqual(node.link, self.linkedList.nodeHead.link)


if __name__ == '__main__':
    unittest.main()

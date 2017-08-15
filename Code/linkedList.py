import os

class myExc(Exception): print "Exception! Your file contains non-numeric information"

class LinkedList(object):
    def __init__(self):
        nodeHead = None
    def createLinkedList(self):
        self.nodeHead = Node()
        self.nodeHead.createNode(0, None)
    

class Node(object):
    def __init__(self):
        data = None
        link = None
    def createNode(self, data, link):
        self.data = data
        self.link = link
    def changeLink(self, node):
        self.link = node
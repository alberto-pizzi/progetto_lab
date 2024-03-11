
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    #head insert
    def addElement(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
    def printList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.next



#Testing implementation
myList = LinkedList()
myList.addElement(10)
myList.addElement(12)
myList.addElement(15)
myList.printList()
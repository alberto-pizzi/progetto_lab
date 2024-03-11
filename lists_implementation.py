
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    #head insert
    def addElement(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.length += 1
    def printList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.next
    #FIXME improve value not found case
    def searchElement(self, value):
        currentNode = self.head
        while currentNode.value != None and currentNode.value != value:
            currentNode = currentNode.next
        return currentNode.value
    def maxElement(self):
        if not self.head:
            return None
        max = self.head.value
        currentNode = self.head.next
        while currentNode:
            if currentNode.value > max:
                max = currentNode.value
            currentNode = currentNode.next
        return max
    def minElement(self):
        if not self.head:
            return None
        min = self.head.value
        currentNode = self.head.next
        while currentNode:
            if currentNode.value < min:
                min = currentNode.value
            currentNode = currentNode.next
        return min

class SortedLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
    #adds elements in grow way
    def addElement(self, value):
        newNode = Node(value)
        self.length += 1
        if not self.head or value < self.head.value:
            newNode.next = self.head
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next and currentNode.next.value < value:
                currentNode = currentNode.next
            newNode.next = currentNode.next
            currentNode.next = newNode
    def minElement(self):
        if not self.head:
            return None
        else:
            return self.head.value
    def median(self):
        if not self.head:
            return None
        if self.length == 1:
            return self.head.value
        medianIndex = self.length // 2
        currentNode = self.head
        for i in range(medianIndex-1):
            currentNode = currentNode.next
        if self.length % 2 == 0:
            return (currentNode.value + currentNode.next.value) / 2
        else:
            return currentNode.next.value


#Testing implementation
myList = SortedLinkedList()
myList.addElement(30)
myList.addElement(10)
myList.addElement(16)
myList.addElement(12)
myList.addElement(40)
myList.addElement(50)
myList.addElement(15)
myList.printList()
print("trova mediana:")
print(myList.median())
"""
print("trova max:")
print(myList.maxElement())
print("trova min:")
print(myList.minElement())
"""
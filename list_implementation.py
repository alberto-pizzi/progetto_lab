
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


#Testing implementation
myList = LinkedList()
myList.addElement(30)
myList.addElement(10)
myList.addElement(12)
myList.addElement(15)
myList.printList()
print("trova max:")
print(myList.maxElement())
print("trova min:")
print(myList.minElement())
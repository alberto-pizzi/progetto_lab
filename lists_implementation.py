
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    #TODO remove them if not useful
    def getValue(self):
        return self.value

    def getNextNode(self):
        return self.next

    def setValue(self, value):
        self.value = value

    def setNextNode(self, nextNode):
        self.next = nextNode
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    #Inserts the new element into the head
    def addElement(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    #Prints full list
    def printList(self):
        currentNode = self.head
        posCounter = 1
        while currentNode:
            print("pos", posCounter, ": ",currentNode.value)
            currentNode = currentNode.next
            posCounter += 1

    #Searches element inside list from input value
    def searchElement(self, value):
        currentNode = self.head
        while currentNode is not None:
            if currentNode.value == value:
                return True
            currentNode = currentNode.next
        return False

    # Searches and returns max element from list (not sorted)
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

    #Searches and returns min element from list (not sorted)
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

    #Adds elements in grow way
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

    #Returns min element from sorted list (growing way)
    def minElement(self):
        if not self.head:
            return None
        else:
            return self.head.value

    #Returns median element from sorted list
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

    #Returns k-th smallest element from sorted list
    def osSelect(self,k):
        if k > self.length:
            return None
        currentNode = self.head
        i = 1
        while i < k and currentNode:
            i += 1
            currentNode = currentNode.next
        return currentNode.value
    def osRank(self,value):
        tmpRank = 0
        currentNode = self.head
        while currentNode is not None:
            tmpRank += 1
            if currentNode.value == value:
                return tmpRank
            currentNode = currentNode.next
        return 0


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
print("trova minimo:")
print(myList.minElement())
print("nodo con terza chiave più piccola")
print(myList.osSelect(2))
print("Ricerca valore 2")
print(myList.searchElement(40))
print("Rango di 1: ")
print(myList.osRank(1))
"""
print("trova max:")
print(myList.maxElement())
print("trova min:")
print(myList.minElement())
"""
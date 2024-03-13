import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    # TODO remove them if not useful
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

    # Returns list length (calculating it)
    def _size(self):
        currentNode = self.head
        count = 0
        while currentNode:
            count += 1
            currentNode = currentNode.getNextNode()
        return count

    def testLength(self):
        if self.length == self._size():
            print("\nLength is right, that is: ", self.length)
        else:
            print("\nLength is wrong")


    # Inserts the new element into the head
    def addElement(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    # Prints full list
    def printList(self):
        currentNode = self.head
        posCounter = 1
        while currentNode:
            print("pos", posCounter, ": ",currentNode.value)
            currentNode = currentNode.next
            posCounter += 1

    # Searches element inside list from input value
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

    # Searches and returns min element from list (not sorted)
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
    def testMinSearching(self,expectedValue):
        if (self.minElement() == expectedValue):
            print("Min finding is right. Min is ", expectedValue)
        else:
            print("Min finding is wrong")
    def testMaxSearching(self,expectedValue):
        if (self.maxElement() == expectedValue):
            print("Max finding is right. Min is ", expectedValue)
        else:
            print("Max finding is wrong")


class SortedLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    # Adds elements in grow way
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

    # Returns min element from sorted list (growing way)
    def minElement(self):
        if not self.head:
            return None
        else:
            return self.head.value
    # Returns median element from sorted list
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

    # Returns k-th smallest element from sorted list
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
        currentNode = self.head
        rank = 0
        while currentNode:
            rank += 1
            if (currentNode.value == value):
                return rank
            currentNode = currentNode.getNextNode()
        return rank

    def testMedian(self,valueExpected):
        if self.median() == valueExpected:
            print("Median expected is right, that is", valueExpected)
        else:
            print("Median expected is wrong")
    def testOSSelect(self,inputOSSelect,valueExpected):
        if self.osSelect(inputOSSelect) == valueExpected:
            print("The result is right, that is", valueExpected)
        else:
            print("The result is wrong")
    def testOSRank(self, inputOSRank, valueExpected):
        if self.osRank(inputOSRank) == valueExpected:
            print("The result (rank) is right, that is", valueExpected)
        else:
            print("The result (rank) is wrong")


#Tests linked lists or sorted linked lists (length, search, insert)
def testLinkedList(linkedList):
    # Creates list of random length
    if type(linkedList) == SortedLinkedList:
        print("\n--------Sorted linked list test--------\n")
    else:
        print("\n--------Linked list (not sorted) test--------\n")
    print("\nList :\n")
    for i in range(random.randint(20, 100)):
        linkedList.addElement(random.randint(0, 1000))
    linkedList.printList()
    # Test length
    print("\nTest length:")
    linkedList.testLength()
    linkedList.addElement(random.randint(1, 1000))
    print("Now, we add a new value and re-test length:")
    linkedList.testLength()

    # Tests search
    valueNotInList = 1500
    valueInList = 500
    print("\n",valueNotInList,"is in the list? ",linkedList.searchElement(valueNotInList))
    linkedList.addElement(valueInList)
    print("\n",valueInList,"is in the list? ",linkedList.searchElement(valueInList))

# This function create another specific list
def testOSSortedLinkedList():
    # Test values
    numEven = 10
    minElement = 1
    medianExpectedFromEven = 5.5
    medianExpectedFromOdd = 6
    medianNotExpected = 15


    # Tests OS implementations with specific sorted linked list
    print("\n--------OS test for sorted linked list--------\n")
    evenLengthList = SortedLinkedList()
    oddLengthList = SortedLinkedList()

    print("Test values are:")
    print("\nMin expected:", minElement, "\nMedian expected from even length:", medianExpectedFromEven)
    print("\nMedian NOT expected:", medianNotExpected, "\nMedian expected from odd length:", medianExpectedFromOdd)
    #Fills lists
    for i in range(minElement,numEven+1):
        evenLengthList.addElement(i)
        oddLengthList.addElement(i)
    oddLengthList.addElement(numEven + 1)
    # List of even length
    print("\nList of even length :\n")
    evenLengthList.printList()
    print("\nTests median from even length list:")
    evenLengthList.testMedian(medianExpectedFromEven)
    print("\nTests median from even length list with unexpected value:")
    evenLengthList.testMedian(medianNotExpected)

    # List of odd length
    print("\nList of odd length :\n")
    oddLengthList.printList()
    print("\nTests median from odd length list:")
    oddLengthList.testMedian(medianExpectedFromOdd)
    print("\nTests median from odd length list with UNEXPECTED value:")
    oddLengthList.testMedian(medianNotExpected)

    # Test min value finding for sorted linked list.
    # The following tests are made ONLY FOR ONE list, because length of list is not relevant
    evenLengthList.testMinSearching(minElement)
    # Test max value finding for sorted linked list.
    evenLengthList.testMaxSearching(numEven)

    # Tests OS-select
    inputOSSelect = 3
    expectedValue = 3
    notExpectedValue = 2*inputOSSelect

    print("\nTest OS-select with expected value (",expectedValue,") from sorted linked list:")
    evenLengthList.testOSSelect(inputOSSelect, expectedValue)
    print("\nTest OS-select with NOT expected value (",notExpectedValue,") from sorted linked list:")
    evenLengthList.testOSSelect(inputOSSelect, notExpectedValue)

    # Tests OS-rank (return position, rank, of value)

    inputOSRank = 3
    expectedRank = 3
    notExpectedRank = 2*inputOSRank

    print("\nTest OS-rank with expected value (",expectedRank, ") from sorted linked list:")
    evenLengthList.testOSRank(inputOSRank, expectedRank)
    print("\nTest OS-rank with NOT expected value (",notExpectedRank,") from sorted linked list:")
    evenLengthList.testOSRank(inputOSRank, notExpectedRank)

def testOSLinkedList():
    # Test values
    maxElement = 100
    minElement = 1


    # Tests OS implementations with specific sorted linked list
    print("\n--------OS test for NOT sorted linked list--------\n")
    linkedList = LinkedList()

    print("\n Min e Max element expected are:",minElement,"and ",maxElement,"\n")
    # Insert max and min value into the list
    linkedList.addElement(maxElement)
    linkedList.addElement(minElement)

    print("\nList :\n")
    for i in range(random.randint(20, 100)):
        linkedList.addElement(random.randint(minElement, maxElement))
    # The max and min inserted from keyboard into list are inside it, so we can test finding
    linkedList.printList()

    # Test max and min values
    linkedList.testMinSearching(minElement)
    linkedList.testMaxSearching(maxElement)

if __name__ == "__main__":
    # FIXME remove comments
    # Test lists
    linkedList = LinkedList()
    testLinkedList(linkedList)
    sortedList = SortedLinkedList()
    testLinkedList(sortedList)

    # Test OS for each list
    testOSLinkedList()
    testOSSortedLinkedList()
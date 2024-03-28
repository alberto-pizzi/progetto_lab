import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

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
            currentNode = currentNode.next
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
            print("Max finding is right. Max is ", expectedValue)
        else:
            print("Max finding is wrong")

    def osSelect(self,k):
        if k > self.length or k <= 0:
            return None
        rank = 0
        # selection-sort
        currentNode = self.head
        while currentNode:
            minNode = currentNode
            nextNode = currentNode.next
            while nextNode:
                if nextNode.value < minNode.value:
                    minNode = nextNode
                nextNode = nextNode.next
            if minNode != currentNode:
                currentNode.value, minNode.value = minNode.value, currentNode.value
            rank += 1
            if rank == k:
                return currentNode.value
            currentNode = currentNode.next
        return None

    def osRank(self, value):
        if not self.head:
            return None
        rank = 0
        # selection-sort
        currentNode = self.head
        while currentNode:
            minNode = currentNode
            nextNode = currentNode.next
            while nextNode:
                if nextNode.value < minNode.value:
                    minNode = nextNode
                nextNode = nextNode.next
            if minNode != currentNode:
                currentNode.value, minNode.value = minNode.value, currentNode.value
            rank += 1
            if currentNode.value == value:
                return rank
            currentNode = currentNode.next
        return 0

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
        if self.head is None:
            return None
        else:
            return self.head.value

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
            currentNode = currentNode.next
        return rank


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
def testOSSortedLinkedList(linkedList):
    # Test values
    length = 10
    minElement = 1


    if type(linkedList) == SortedLinkedList:
        print("\n--------OS-select and rank test for sorted linked list--------\n")
    else:
        print("\n--------OS-select and rank  test for NOT sorted linked list--------\n")
        print("\nThe values in the not sorted list are inserted in descending order, so they will be increasing\n")

    # Tests OS implementations with specific sorted linked list

    print("Test values are:")
    print("\nMin expected:", minElement)
    #Fills list
    for i in range(length,minElement-1,-1):
        linkedList.addElement(i)
    # List of even length
    print("\nList of even length :\n")
    linkedList.printList()


    # Test min value finding for sorted linked list.
    linkedList.testMinSearching(minElement)
    # Test max value finding for sorted linked list.
    linkedList.testMaxSearching(length)

    # Tests OS-select
    inputOSSelect = 3
    expectedValue = 3
    notExpectedValue = 2*inputOSSelect

    print("\nTest OS-select with expected value (",expectedValue,") from sorted linked list:")
    linkedList.testOSSelect(inputOSSelect, expectedValue)
    print("\nTest OS-select with NOT expected value (",notExpectedValue,") from sorted linked list:")
    linkedList.testOSSelect(inputOSSelect, notExpectedValue)

    # Tests OS-rank (return position, rank, of value)

    inputOSRank = 3
    expectedRank = 3
    notExpectedRank = 2*inputOSRank

    print("\nTest OS-rank with expected value (",expectedRank, ") from sorted linked list:")
    linkedList.testOSRank(inputOSRank, expectedRank)
    print("\nTest OS-rank with NOT expected value (",notExpectedRank,") from sorted linked list:")
    linkedList.testOSRank(inputOSRank, notExpectedRank)

def testMaxAndMinSearch(linkedList):
    # Test values
    maxElement = 100
    minElement = 1


    if type(linkedList) == SortedLinkedList:
        print("\n--------Max and Min test for sorted linked list--------\n")
    else:
        print("\n--------Max and Min  test for NOT sorted linked list--------\n")

    # Tests OS implementations with specific linked list (sorted or not)

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

    # Test lists
    linkedList1 = LinkedList()
    testLinkedList(linkedList1)
    sortedList1 = SortedLinkedList()
    testLinkedList(sortedList1)

    # Test OS for each list
    linkedList2 = LinkedList()
    sortedList2 = SortedLinkedList()
    testMaxAndMinSearch(linkedList2)
    testMaxAndMinSearch(sortedList2)
    linkedList3 = LinkedList()
    sortedList3 = SortedLinkedList()
    testOSSortedLinkedList(linkedList3)
    testOSSortedLinkedList(sortedList3)

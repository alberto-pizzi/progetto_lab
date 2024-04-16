import random
import numpy as np
import math
from abc import ABC, abstractmethod

def swap(a,b):
    return (b,a)

class Heap(ABC):
    def __init__(self):
        self.size = 0
        self.heap = []
    #Return position of i's parent
    def parentPos(self,pos):
        if self.size > 0:
            return (pos-1) // 2
    def leftChildPos(self,pos):
        childPos = (2 * pos)+1
        if self.size > 0:
            return childPos
    def rightChildPos(self,pos):
        childPos = (2 * pos)+2
        if self.size > 0:
            return childPos
    def printHeap(self):
        #print ("Print heap: ")
        print("\n",self.heap, end=" ")

    @abstractmethod
    def heapify(self,pos):
        pass

    @abstractmethod
    def editKey(self,i,value):
        pass
    def extractRoot(self):
        if self.size < 1:
            return None
        rootValue = self.heap[0]
        lastValue = self.heap[self.size-1]
        self.heap[0] = lastValue
        del self.heap[self.size-1]
        self.size -= 1
        if self.size > 1:
            self.heapify(0)
        return rootValue
    def buildHeap(self,a):
        self.size = len(a)
        self.heap = a
        start_index = (len(a)//2)-1
        for i in range(start_index,-1,-1):
            self.heapify(i)
    #return max or min value of the heap
    def _rootValue(self):
        if self.size > 0:
            return self.heap[0]
        else:
            print("Heap is empty")
            return

    def minimum(self):
        if self.size > 0:
            middle = math.ceil(self.size/2)
            minimum = self.heap[middle]
            for i in range(middle,self.size):
                if self.heap[i] < minimum:
                    minimum = self.heap[i]
            return minimum
        else:
            print("Heap is empty")
            return
    def maximum(self):
        if self.size > 0:
            middle = math.ceil(self.size/2)
            maximum = self.heap[middle]
            for i in range(middle,self.size):
                if self.heap[i] > maximum:
                    maximum = self.heap[i]
            return maximum
        else:
            print("Heap is empty")
            return

    #extracts the root, so is not re-usable
    def osRank(self, value):
        tmpRank = 0
        root = self.extractRoot()
        while tmpRank < self.size:
            if root == value:
                return tmpRank+1
            else:
                tmpRank += 1
                root = self.extractRoot()
        return 0

    def insert(self, value):
        self.size += 1
        self.heap = np.append(self.heap,True)
        self.editKey(self.size-1, value)

    def osSelect(self,k):
        if self.size <= 0 or k < 1 or k > self.size:
            return None
        for i in range(k):
            root = self.extractRoot()
        return root

    def testParentPos(self, valuePos, parentExpected):
        if parentExpected == self.heap[self.parentPos(valuePos - 1)]:
            print("Parent is right.")
        else:
            print("Parent is wrong.")
    def testRightChildPos(self, valuePos, childExpected):
        if childExpected == self.heap[self.rightChildPos(valuePos - 1)]:
            print("Right child is right.")
        else:
            print("Right child is wrong.")

    def testLeftChildPos(self, valuePos, childExpected):
        if childExpected == self.heap[self.leftChildPos(valuePos - 1)]:
            print("Left child is right.")
        else:
            print("Left child is wrong.")
    def testRoot(self,rootExpected):
        if rootExpected == self._rootValue():
            print("Root is right.")
        else:
            print("Root is wrong.")

class Maxheap(Heap):
    def __init__(self):
        super().__init__()
    def editKey(self, i, value):
        if not self.heap[i] or value < self.heap[i]:
            print("New key is lower than the old one")
            return
        self.heap[i] = value
        while (i > 0) and (self.heap[self.parentPos(i)] < self.heap[i]):
            self.heap[i],self.heap[self.parentPos(i)] = swap(self.heap[i],self.heap[self.parentPos(i)])
            i = self.parentPos(i)
    def heapify(self, pos):
        left = self.leftChildPos(pos)
        right = self.rightChildPos(pos)
        if (left < self.size) and (self.heap[left] > self.heap[pos]):
            maxValuePos = left
        else:
            maxValuePos = pos
        if (right < self.size) and (self.heap[right] > self.heap[maxValuePos]):
            maxValuePos = right
        if maxValuePos != pos:
            self.heap[pos],self.heap[maxValuePos] = swap(self.heap[pos],self.heap[maxValuePos])
            self.heapify(maxValuePos)
    def maximum(self):
        return super()._rootValue()

class Minheap(Heap):
    def __init__(self):
        super().__init__()
    def editKey(self, i, value):
        if value > self.heap[i]:
            print("New key is bigger than the old one")
            return
        self.heap[i] = value
        while (i > 0) and (self.heap[self.parentPos(i)] > self.heap[i]):
            self.heap[i],self.heap[self.parentPos(i)] = swap(self.heap[i],self.heap[self.parentPos(i)])
            i = self.parentPos(i)

    def heapify(self, pos):
        left = self.leftChildPos(pos)
        right = self.rightChildPos(pos)
        if (left < self.size) and (self.heap[left] < self.heap[pos]):
            minValuePos = left
        else:
            minValuePos = pos
        if (right < self.size) and (self.heap[right] < self.heap[minValuePos]):
            minValuePos = right
        if minValuePos != pos:
            self.heap[pos],self.heap[minValuePos] = swap(self.heap[pos],self.heap[minValuePos])
            self.heapify(minValuePos)

    def minimum(self):
        return super()._rootValue()

def testHeaps():
    minHeap = Minheap()
    maxHeap = Maxheap()

    totElements = 100

    arr1 = []
    arr2 = []
    for i in range(totElements):
        arr1.append(i+1)
        arr2.append(arr1[i])
    maxArr = max(arr1)
    minArr = min(arr1)

    minHeap.buildHeap(arr1)
    maxHeap.buildHeap(arr2)

    minHeap.printHeap()
    maxHeap.printHeap()
    print("\n--------test Heaps implementations--------\n")


    print("\n------test Min-heap------\n")
    minHeap.testRoot(minArr)
    minHeap.testParentPos(2,1)
    minHeap.testLeftChildPos(2,4)
    minHeap.testRightChildPos(2,5)

    print("\n------test Max-heap------\n")
    maxHeap.testRoot(maxArr)
    maxHeap.testParentPos(2,100)
    maxHeap.testLeftChildPos(2,79)
    maxHeap.testRightChildPos(2,94)


def testMaxAndMinHeaps():
    minHeap = Minheap()
    maxHeap = Maxheap()

    totElements = 100

    arr1 = []
    arr2 = []
    for i in range(totElements):
        arr1.append(random.randint(1, 200))
        arr2.append(arr1[i])
    maxArr = max(arr1)
    minArr = min(arr1)

    minHeap.buildHeap(arr1)
    maxHeap.buildHeap(arr2)

    print("\n--------Max and Min test for heaps--------\n")

    print("\nPrint min-heap: ")
    minHeap.printHeap()
    print("\nPrint max-heap: ")
    maxHeap.printHeap()

    print("\n\nmin: ",minArr)
    print("\nmax: ",maxArr)

    if maxArr == maxHeap.maximum() and maxArr == minHeap.maximum():
        print("Maximums is right.")
    else:
        print("Maximums is wrong")

    if minArr == maxHeap.minimum() and minArr == minHeap.minimum():
        print("Minimums is right.")
    else:
        print("Minimums is wrong")

def testOSselectOSrankMinHeap():
    minHeap1 = Minheap()
    minHeap2 = Minheap()
    totElements = 100

    arr1 = []
    arr2 = []
    for i in range(totElements):
        arr1.append(i+1)
        arr2.append(i+1)

    maxArr = max(arr1)
    minArr = min(arr1)

    minHeap1.buildHeap(arr1)
    minHeap2.buildHeap(arr2)

    print("\n--------OS-select and OS-rank test for Min-heap--------\n")

    rank = 2
    value = 2
    expectedSelectValue = 2
    expectedRank = 2

    if expectedSelectValue == minHeap1.osSelect(rank):
        print("OS-select is correct")
    else:
        print("OS-select is wrong")

    if expectedRank == minHeap2.osRank(value):
        print("OS-rank is correct")
    else:
        print("OS-rank is wrong")


if __name__ == "__main__":
    testHeaps()
    testMaxAndMinHeaps()
    testOSselectOSrankMinHeap()

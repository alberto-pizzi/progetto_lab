import math
import numpy as np

def swap(a,b):
    return (b,a)

class Heap:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = np.array([])
    #Return position of i's parent
    def parentPos(self,pos):
        if self.size > 0:
            return math.floor((pos-1) / 2)
    def leftChildPos(self,pos):
        childPos = (2 * pos)+1
        if self.size > 0:
            return childPos
    def rightChildPos(self,pos):
        childPos = (2 * pos)+2
        if self.size > 0:
            return childPos
    def printHeap(self):
        print ("Print heap: ")
        print(self.heap, end=" ")

class Maxheap(Heap):
    def heapMaximum(self):
        if self.size > 0:
            return self.heap[0]
        else:
            print("Heap is empty")
            return
    def heapIncreaseKey(self,i,value):
        if value < self.heap[i]:
            print("New key is lower than the old one")
            return
        self.heap[i] = value
        while (i > 0) and (self.heap[self.parentPos(i)]):
            self.heap[i],self.heap[self.parentPos(i)] = swap(self.heap[i],self.heap[self.parentPos(i)])
            i = self.parentPos(i)

#FIXME overflow index
    def heapInsert(self,value):
            if self.size >= self.maxsize:
                print("Heap is full")
                return
            self.size += 1
            self.heap[self.size-1] = value
            self.heapIncreaseKey(self.size-1,value)

    def maxHeapify(self,pos):
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
            self.maxHeapify(maxValuePos)

    def buildMaxHeap(self,a):
        self.size = len(a)
        self.heap = a
        start_index = math.floor(len(a)/2)-1
        for i in range(start_index,-1,-1):
            self.maxHeapify(i)

    def heapExtractMax(self):
        if self.size < 1:
            return None
        maxValue = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.size -= 1
        self.maxHeapify(0) #FIXME
        return maxValue

#TODO implment it for min-heap
    #optimized os-rank with O(rank)
    def _rankR(self, target, currentNodeIndex):
        currentNodeValue = self.heap[currentNodeIndex]
        if currentNodeValue >= target:
            lValue = 0
            rValue = 0
            if self.leftChildPos(currentNodeIndex) < self.size:
                lValue = self._rankR(target, self.leftChildPos(currentNodeIndex))
            if self.rightChildPos(currentNodeIndex) < self.size:
                rValue = self._rankR(target, self.rightChildPos(currentNodeIndex))
            return lValue + rValue + 1
        return 0


    def osRank(self, target):
        if self.size > 0:
            return self._rankR(target, 0)
        else:
            return 0


#TODO remove these tests
"""
h1 = Maxheap(10)
arr = np.array([4,1,3,2,16,9,10,14,8,7])
print("Stampo array: ",arr)
"""
h1 = Maxheap(10)
#arr = np.array([8,5,10,3,12,7])
arr = np.array([38,203,1,45,39,10,34,90,10,2,100,1])
h1.buildMaxHeap(arr)
h1.printHeap()
"""
while h1.heapMaximum() != 39:
    print(h1.heapExtractMax())
h1.printHeap()
"""
print("Rango di 39: ")
print(h1.osRank(39))

"""
h1 = Maxheap(10)
h1.heapInsert(2)
h1.heapInsert(10)
h1.printHeap()
"""
import array
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

#TODO remove these tests
"""
h1 = Maxheap(10)
arr = np.array([4,1,3,2,16,9,10,14,8,7])
print("Stampo array: ",arr)

h1.buildMaxHeap(arr)
h1.printHeap()
"""


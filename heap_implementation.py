import numpy as np
import math

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

    def heapify(self,pos):
        pass
    def editKey(self,i,value):
        pass
    def extractRoot(self):
        if self.size < 1:
            return None
        rootValue = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.size -= 1
        self.heap = self.heap[:self.size]
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
    def osRankNotOptimized(self,value):
        tmpRank = 0
        root = self.extractRoot()

        while tmpRank < self.size:
            if root == value:
                return tmpRank+1
            else:
                tmpRank += 1
                root = self.extractRoot()
        return 0

    #FIXME fix implementation of array (with dots)
    def insert(self, value):
        if self.size >= self.maxsize:
            print("Heap is full")
            return
        self.size += 1
        self.heap = np.append(self.heap,value)
        self.editKey(self.size-1, value)

class Maxheap(Heap):
    def editKey(self, i, value):
        if value < self.heap[i]:
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
#TODO implment it for min-heap or remove it, fix it
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

    #doesn't extract the root, so is re-usable
    def osRankOptimized(self, target):
        if self.size > 0:
            return self._rankR(target, 0)
        else:
            return 0

class Minheap(Heap):
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


#TODO remove these tests

"""
h1 = Maxheap(10)
arr = np.array([4,1,3,2,16,9,10,14,8,7])

print("Stampo array: ",arr)
h1.buildHeap(arr)
h1.printHeap()
print("lunghezza array: ", len(h1.heap))

h1 = Maxheap(12)
#arr = np.array([8,5,10,3,12,7])
arr = np.array([38,203,1,45,39,10,34,90,10,2,100,1])
h1.buildHeap(arr)
h1.printHeap()
print("lunghezza heap: ", len(h1.heap))
"""
h1 = Maxheap(10)
h1.insert(4)
h1.insert(1)
h1.insert(3)
h1.insert(2)
h1.insert(16)
h1.insert(9)
h1.insert(10)
h1.insert(14)
h1.insert(8)
h1.insert(7)
print("Stampa heap: ")
h1.printHeap()


h2 = Maxheap(10)
arr = np.array([4,1,3,2,16,9,10,14,8,7])
h2.buildHeap(arr)
print("Stampa heap: ")
h2.printHeap()
print("\n Trova il minimo: ")
print(h2.minimum())
print("\n Trova il max: ")
print(h2.maximum())

h3 = Minheap(3)
h3.insert(3)
h3.insert(2)
h3.insert(16)
print("\n Trova il minimo: ")
print(h3.minimum())
print("\n Trova il max: ")
print(h3.maximum())

"""
while h1.heapMaximum() != 39:
    print(h1.heapExtractMax())
h1.printHeap()

print("Rango di 39: ")
print(h1.osRank(39))
h1 = Maxheap(10)
h1.insert(2)
h1.insert(10)
h1.printHeap()
"""

print("\n Rango di 1: ")
#print(h1.osRankNotOptimized(100))
#print(h1.osRankOptimized(1))

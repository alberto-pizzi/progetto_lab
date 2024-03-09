import math

def swap(a,b):
    return (b,a)

class Maxheap:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = []

    def heapMaximum(self):
        if self.size > 0:
            return self.heap[0]
        else:
            print("Heap is empty")
            return

    def heapInsert(self,value):
            if self.size >= self.maxsize:
                print("Heap is full")
                return
            self.size += 1
            self.heap[self.size] = value
            self.heapIncreaseKey(self.size,value)

    #Return position of i's parent
    def parentPos(self,i):
        if self.size > 0:
            return math.floor(i/2)

    def heapIncreaseKey(self,i,value):
        if value < self.heap[i]:
            print("New key is lower than the old one")
            return
        self.heap[i] = value
        while (i > 0) and (self.heap[self.parentPos(i)]):
            self.heap[i],self.heap[self.parentPos(i)] = swap(self.heap[i],self.heap[self.parentPos(i)])
            i = self.parentPos(i)


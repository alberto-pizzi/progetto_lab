import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np
import math

def randomList(totElements):
    newList = []
    maxNum = totElements * 10
    for i in range(totElements):
        newList.append(random.randint(0, maxNum)/divider(maxNum))
    return newList

def divider(totElements):
    numDigits = len(str(totElements))
    dividerStr = "1" + ("0" * (numDigits))
    dividerInt = int(dividerStr)
    return dividerInt

def growerList(totElements):
    newList = []
    for i in range(totElements):
        newList.append(i/divider(totElements))
    return newList

def descendingList(totElements):
    newList = []
    for i in range(totElements,-1,-1):
        newList.append(i/divider(totElements))
    return newList

def insertionSort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

def bucketSort(a):
    n = len(a)
    b = [None] * n
    for i in range(n):
        b[i] = []
    for i in range(n):
        b[math.floor(n * a[i])].append(a[i])
    for i in range(n):
        insertionSort(b[i])
    return [x for sublist in b for x in sublist]


def insertionSortTest(a):
    newList = a
    start = timer()
    insertionSort(newList)
    end = timer()
    time = end - start
    return time

def bucketSortTest(a):
    newList = a
    start = timer()
    bucketSort(newList)
    end = timer()
    time = end - start
    return time


def measurements(values):
    times = []
    for i in range(len(values)):
        timeIS = insertionSortTest(values[i])
        timeBS = bucketSortTest(values[i])
        times.append([timeIS, timeBS])
    return times

def drawGraph(graphTitle, x, y, zoom=False, zoomGrade=20):
    yIS = []
    yBS = []
    for i in range(y.shape[0]):
        yIS.append(y[i, 0, 0])
        yBS.append(y[i, 0, 1])


    if zoom:
        title = graphTitle + ' zoom ' + str(zoomGrade) + 'x'
        maxEl = np.max(y)
        # set zoom scale
        plt.ylim(0,maxEl/zoomGrade)
    else:
        title = graphTitle

    plt.title(title)
    plt.xlabel("Numero di elementi")
    plt.ylabel("Tempi (s)")
    plt.plot(x, yIS, color='blue', label='Insertion-sort')
    plt.plot(x, yBS, color='red', label='Bucket-sort')
    plt.legend()
    plt.show()

def runAllTests():
    nIterations = 20
    #x = [50,250,500,1000,5000,12000]
    x = [g for g in range(50, 1050, 100)]
    finalTimes = np.array([])
    for j in x:
        allTimes = []
        for i in range(nIterations):
            values = []
            values.append(randomList(j))
            values.append(growerList(j))
            values.append(descendingList(j))
            print("\nTest: ",i+1,"with ",j," elements")
            times = measurements(values)
            allTimes.append(times)
        # Calculates average
        allTimes = np.sum(allTimes, axis=0)
        allTimes = np.divide(allTimes, nIterations)
        finalTimes = np.append(finalTimes, allTimes)

    finalTimes = finalTimes.reshape(len(x), 3, 2)

    drawGraph("Insertion-sort vs Bucket-sort (valori random)", x, finalTimes[:, :1, :])
    drawGraph("Insertion-sort vs Bucket-sort (valori crescenti)", x, finalTimes[:, 1:2, :])
    drawGraph("Insertion-sort vs Bucket-sort (valori decrescenti)", x, finalTimes[:, 2:, :])
    drawGraph("Insertion-sort vs Bucket-sort (valori random)", x, finalTimes[:, :1, :],True)
    drawGraph("Insertion-sort vs Bucket-sort (valori decrescenti)", x, finalTimes[:, 2:, :],True)


if __name__ == "__main__":
    runAllTests()

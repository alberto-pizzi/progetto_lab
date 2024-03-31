import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np
import math
import copy

"""
def divider(totElements):
    numDigits = len(str(totElements))
    dividerStr = "1" + ("0" * (numDigits))
    dividerInt = int(dividerStr)
    return dividerInt

def randomList(totElements):
    newList = []
    maxNum = 10000
    for i in range(totElements):
        newList.append(random.randint(0, maxNum)/divider(maxNum))
        #newList.append(random.random())
    return newList

def listWithSameValues(totElements,value):
    newList = []
    for i in range(totElements):
        newList.append(value/divider(value))
    return newList
"""
def randomList(totElements):
    newList = []
    #maxNum = 10000
    for i in range(totElements):
        #newList.append(random.randint(0, maxNum)/divider(maxNum))
        newList.append(random.random())
    return newList

def forceValue(totElements, value):
    numDigits = len(str(totElements))
    convertingStr = "0." + ("0" * (numDigits)) + str(value)
    convertedInt = float(convertingStr)
    return convertedInt

def generateUniqueBucketRandList(totElements):
    newList = []
    maxNum = 10000
    for i in range(totElements):
        newList.append(forceValue(totElements, random.randint(1, maxNum)))
        #newList.append(converter(totElements,i))
    return newList

def generateUniqueBucketGrowingList(totElements):
    newList = []
    for i in range(totElements):
        newList.append(forceValue(totElements, i))
        #newList.append(converter(totElements,i))
    return newList

def generateUniqueBucketDecreasingList(totElements):
    newList = []
    for i in range(totElements,-1,-1):
        newList.append(forceValue(totElements, i))
        #newList.append(converter(totElements,i))
    return newList

def generateRandomUniqueValues(totElements):
    # Genera totElements valori univoci distribuiti uniformemente nell'intervallo [0, 1) e  li mescola
    values = [(i + 0.5) /totElements for i in range(totElements)]
    random.shuffle(values)
    return values




def growerList(totElements):
    """
    newList = []
    for i in range(totElements):
        newList.append(i/divider(totElements))
    return newList
    """
    return [i/totElements for i in range(totElements)]

def descendingList(totElements):
    """
    newList = []
    for i in range(totElements,-1,-1):
        newList.append(i/divider(totElements))
    return newList
    """
    return [1 - i / totElements for i in range(1, totElements)]

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
    valuesIS = copy.deepcopy(values)
    valuesBS = copy.deepcopy(values)
    for i in range(len(values)):
        timeIS = insertionSortTest(valuesIS[i])
        timeBS = bucketSortTest(valuesBS[i])
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
    nIterations = 100
    totalTypesOfValues = 7
    #x = [50,250,500,1000,5000,12000]
    x = [g for g in range(50, 1050, 100)]
    finalTimes = np.array([])
    for j in x:
        allTimes = []
        for i in range(nIterations):
            values = []
            values.append(generateRandomUniqueValues(j))
            values.append(growerList(j))
            values.append(descendingList(j))
            values.append(generateUniqueBucketRandList(j))
            values.append(generateUniqueBucketGrowingList(j))
            values.append(generateUniqueBucketDecreasingList(j))
            values.append(randomList(j))
            print("\nTest: ",i+1,"with ",j," elements")
            times = measurements(values)
            allTimes.append(times)
        # Calculates average
        allTimes = np.sum(allTimes, axis=0)
        allTimes = np.divide(allTimes, nIterations)
        finalTimes = np.append(finalTimes, allTimes)

    finalTimes = finalTimes.reshape(len(x), totalTypesOfValues, 2)

    drawGraph("Insertion-sort vs Bucket-sort (valori random uniformi)", x, finalTimes[:, :1, :])
    drawGraph("Insertion-sort vs Bucket-sort (valori random uniformi)", x, finalTimes[:, :1, :],True)

    drawGraph("Insertion-sort vs Bucket-sort (valori crescenti)", x, finalTimes[:, 1:2, :])
    drawGraph("Insertion-sort vs Bucket-sort (valori decrescenti)", x, finalTimes[:, 2:3, :])
    drawGraph("Insertion-sort vs Bucket-sort (valori decrescenti)", x, finalTimes[:, 2:3, :],True)

    drawGraph("Insertion-sort vs Bucket-sort (valori in un bucket,rand)", x, finalTimes[:, 3:4, :])
    drawGraph("Insertion-sort vs Bucket-sort (valori in un bucket,crescenti)", x, finalTimes[:, 4:5, :])
    drawGraph("Insertion-sort vs Bucket-sort (valori in un bucket,decrescenti)", x, finalTimes[:, 5:6, :])

    drawGraph("Insertion-sort vs Bucket-sort (valori random, distr. random)", x, finalTimes[:, 6:, :])
    drawGraph("Insertion-sort vs Bucket-sort (valori random, distr. random)", x, finalTimes[:, 6:, :],True)
    #drawGraph("Insertion-sort vs Bucket-sort ()", x, finalTimes[:, :1, :])


if __name__ == "__main__":
    runAllTests()

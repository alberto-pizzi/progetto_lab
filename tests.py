
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import bst_implementation as BST
import lists_implementation as LL
import heap_implementation as HP
import random
import math

def generateRandomValues(start,totalValues, minRandomValue, maxRandomValue):
    randomValues = []
    for i in range(start,totalValues):
         randomValues.append(random.randint(minRandomValue,maxRandomValue))
    return randomValues

def generateIncreasingValues(minValue, maxValue):
    values = []
    for i in range(minValue, maxValue + 1):
        values.append(i)
    return values

def generateDecreasingValues(maxValue, minValue):
    values = []
    for i in range(maxValue, minValue-1,-1):
        values.append(i)
    return values

# FIXME rivedere se devo dividere per il numero di elementi
def searchMaxBSTTest(values):
    # Create BST with input values
    newBST = BST.BSTree()
    for i in values:
        newBST.insertElement(i)
    #print("\n")
    start = timer()
    maxBST = newBST.nodeMaximum(newBST.root).value
    end = timer()
    time = end - start
    return time


def searchMinBSTTest(values):
    # Create BST with input values
    newBST = BST.BSTree()
    for i in values:
        newBST.insertElement(i)
    start = timer()
    minBST = newBST.nodeMinimum(newBST.root).value
    end = timer()
    time = end-start
    return time

def searchMinMinHeapTest(values):
    # Create Min-heap with input values
    newHeap = HP.Minheap()
    newHeap.buildHeap(values)
    start = timer()
    minBST = newHeap.minimum()
    end = timer()
    time = end-start
    return time

def searchMaxMaxHeapTest(values):
    # Create Max-heap with input values
    newHeap = HP.Maxheap()
    newHeap.buildHeap(values)
    start = timer()
    minBST = newHeap.maximum()
    end = timer()
    time = end-start
    return time

def osRankBSTTest(values, targetValue):
    # Create BST with input values
    newBST = BST.BSTree()
    for i in values:
        newBST.insertElement(i)
    nodeTarget = newBST.searchNode(targetValue)

    start = timer()
    rank = newBST.osRank(nodeTarget)
    end = timer()
    time = end-start
    return time

def osRankMinHeapTest(values, targetValue):
    # Create Min-heap with input values
    newHeap = HP.Minheap()

    newHeap.buildHeap(values)

    start = timer()
    rank = newHeap.osRankNotOptimized(targetValue)
    end = timer()
    time = end-start
    return time

def osSelectBSTTest(values, iPos):
    # Create BST with input values
    newBST = BST.BSTree()
    for i in values:
        newBST.insertElement(i)

    start = timer()
    rank = newBST.osSelect(newBST.root,iPos)
    end = timer()
    time = end-start
    return time

def osSelectMinHeapTest(values, iPos):
    # Create Min Heap with input values
    newHeap = HP.Minheap()

    newHeap.buildHeap(values)

    start = timer()
    rank = newHeap.osSelect(iPos)
    end = timer()
    time = end-start
    return time

def drawGraph(graphTitle, labelHeapType, xValues, testFinalTimes,zoom = False):
    # FIXME
    if testFinalTimes.shape[1] > 2:
        yHeapValues = testFinalTimes[:, :1]
        yLinkedListValues = testFinalTimes[:, 1:2]
        ySortredListValues = testFinalTimes[:, 2:]
    else:
        yHeapValues = testFinalTimes[:, :1]
        ySortredListValues = testFinalTimes[:, 1:]

    graph = plt.figure()
    plt.title(graphTitle)
    #fig,ax=plt.subplots()


    if zoom:
        maxEl = np.max(testFinalTimes)
        plt.ylim(0,maxEl/10)
    #plt.ylim(0,ultimoEl*3)
    #plt.ylim(0, 0.00002)
    #plt.xlim(50,5000)
    #plt.xlim(0,500)
    #ylog= np.log2(rif)
    plt.xlabel("Numero di elementi")
    plt.ylabel("Tempi (s)")
    #plt.plot(xValues, yBstValues, color='red', label='ABR')
    plt.plot(xValues, yHeapValues, color='red', label=labelHeapType)
    if testFinalTimes.shape[1] > 2:
        plt.plot(xValues, yLinkedListValues, color='blue', label='Lista non ordinata')
    plt.plot(xValues, ySortredListValues, color='green', label='Lista ordinata')
    #plt.plot(xValues,rif,color='green',label = 'Rif log2')
    plt.legend()

    """
    x1 = xValues[:2]
    y1 = yBstValues[:2]
    zm = ax.inset_axes([0.1, 0.1, 0.8, 0.8])
    zm.plot(x1,y1)
    zm.indicate_inset_zoom(zm,edgecolor='green',lw=7)
    """

    return graph

def saveGraph(nameFile,graph):
    directory = "Graphs/" + nameFile + ".png"
    graph.savefig(directory)

def searchMaxSLLTest(values):
    newSortedList = LL.SortedLinkedList()
    for i in values:
        newSortedList.addElement(i)

    start = timer()
    maxSLL = newSortedList.maxElement()
    end = timer()
    time = end - start
    return time

def searchMaxLLTest(values):
    newList = LL.LinkedList()
    for i in values:
        newList.addElement(i)

    start = timer()
    minSLL = newList.maxElement()
    end = timer()
    time = end-start
    return time

def searchMinSLLTest(values):
    newSortedList = LL.SortedLinkedList()
    for i in values:
        newSortedList.addElement(i)

    start = timer()
    minSLL = newSortedList.minElement()
    end = timer()
    time = end-start
    return time

def searchMinLLTest(values):
    newList = LL.LinkedList()
    for i in values:
        newList.addElement(i)

    start = timer()
    minSLL = newList.minElement()
    end = timer()
    time = end-start
    return time

def osRankSLLTest(values, targetValue):
    newSortedList = LL.SortedLinkedList()
    for i in values:
        newSortedList.addElement(i)

    start = timer()
    rank = newSortedList.osRank(targetValue)
    end = timer()
    time = end-start
    return time

def osSelectSLLTest(values, iPos):
    newSortedList = LL.SortedLinkedList()
    for i in values:
        newSortedList.addElement(i)

    start = timer()
    rank = newSortedList.osSelect(iPos)
    end = timer()
    time = end-start
    return time

def searchMaxTests(values):
    times = []
    for i in range(len(values)):
        timeHeap = searchMaxMaxHeapTest(values[i])
        timeSLL = searchMaxSLLTest(values[i])
        timeLL = searchMaxLLTest(values[i])
        times.append([timeHeap, timeLL, timeSLL])
    return times
def searchMinTests(values):
    timeHeap = searchMinMinHeapTest(values)
    timeLL = searchMinLLTest(values)
    timeSLL = searchMinSLLTest(values)
    times = [timeHeap, timeLL, timeSLL]
    return times

def oSRankTests(values):
    randomTarget = random.choice(values)
    #randomTarget = values[len(values)-1]
    #print('\nSearching Max in BST test:\n')
    #FIXME
    timeHeap = osRankMinHeapTest(values,randomTarget)
    #print('\nSearching Max in Sorted Linked List test:\n')
    timeSLL = osRankSLLTest(values,randomTarget)
    times = [timeHeap, timeSLL]
    return times

def oSSelectTests(values):
    iPosition = random.randint(1,len(values))
    #print('\nSearching Max in BST test:\n')
    # FIXME
    timeHeap = osSelectMinHeapTest(values,iPosition-1)
    #print('\nSearching Max in Sorted Linked List test:\n')
    timeSLL = osRankSLLTest(values,iPosition)
    times = [timeHeap, timeSLL]
    return times

def runAllTests():
    # FIXME
    n = 150
    totalDataStructures = 3
    #x = [g for g in range(200,2000,200)]
    x = [50,250,1000,5000,15000]
    finalTimesMaxTest = np.array([])
    finalTimesMinTest = np.array([])
    finalTimesOSSelectTest = np.array([])
    finalTimesOSRankTest = np.array([])
    for j in x:
        timesMaxTests = []
        timesMinTests = []
        timesOSSelectTests = []
        timesOSRankTests = []
        for i in range(n):
            values = []
            values.append(generateRandomValues(0, j, 1, 10000))
            values.append(generateIncreasingValues(1, j))
            values.append(generateDecreasingValues(j,1))
            print("\nTest: ",i+1,"with ",j," elements")
            # Maximum
            timesMaxTest = searchMaxTests(values)
            timesMaxTests.append(timesMaxTest)
            # Minimum
            timesMinTest = searchMinTests(values)
            timesMinTests.append(timesMinTest)
            # OS-Select
            timesOSSelectTest = oSSelectTests(values)
            timesOSSelectTests.append(timesOSSelectTest)
            # OS-Rank
            timesOSRankTest = oSRankTests(values)
            timesOSRankTests.append(timesOSRankTest)

        # Maximum
        timesMaxTests = np.sum(timesMaxTests, axis=0)
        timesMaxTests = np.divide(timesMaxTests, n)
        finalTimesMaxTest = np.append(finalTimesMaxTest, timesMaxTests)
        # Minimum
        timesMinTests = np.sum(timesMinTests, axis=0)
        timesMinTests = np.divide(timesMinTests, n)
        finalTimesMinTest = np.append(finalTimesMinTest, timesMinTests)
        # OS-Select
        timesOSSelectTests = np.sum(timesOSSelectTests, axis=0)
        timesOSSelectTests = np.divide(timesOSSelectTests, n)
        finalTimesOSSelectTest = np.append(finalTimesOSSelectTest, timesOSSelectTests)
        # OS-Rank
        timesOSRankTests = np.sum(timesOSRankTests, axis=0)
        timesOSRankTests = np.divide(timesOSRankTests, n)
        finalTimesOSRankTest = np.append(finalTimesOSRankTest, timesOSRankTests)

    # Reshape matrix
    finalTimesMaxTest = finalTimesMaxTest.reshape(len(x), totalDataStructures,3)
    finalTimesMinTest = finalTimesMinTest.reshape(len(x), totalDataStructures)
    finalTimesOSSelectTest = finalTimesOSSelectTest.reshape(len(x), 2)
    finalTimesOSRankTest = finalTimesOSRankTest.reshape(len(x), 2)
    #print("\nfinalTimes:\n",finalTimesMaxTest)

    #print("\n Tempi BST:",finalTimesBST)
    #print("\n Tempi SLL:", finalTimesLL)
    graphMaxRandValues = drawGraph("Cerca Max (random values)",'Max-heap',x,finalTimesMaxTest)
    saveGraph("max_search_with_random_values",graphMaxRandValues)
    #graphMaxRandValues.show()
    graphMinRandValues = drawGraph("Cerca Min (random values)", 'Min-heap', x, finalTimesMinTest)
    saveGraph("min_search_with_random_values", graphMinRandValues)
    graphMinRandValuesZoom = drawGraph("Cerca Min (random values) zoom", 'Min-heap', x, finalTimesMinTest,True)
    saveGraph("min_search_with_random_values_zoom", graphMinRandValuesZoom)


    graphOSSelectRandValues = drawGraph("OS-select (random values)", 'Min-heap', x, finalTimesOSSelectTest)
    saveGraph("os_select_with_random_values", graphOSSelectRandValues)
    graphOSSelectRandValuesZoom = drawGraph("OS-select (random values) zoom", 'Min-heap', x, finalTimesOSSelectTest,True)
    saveGraph("os_select_with_random_values_zoom", graphOSSelectRandValuesZoom)

    graphOSRankRandValues = drawGraph("OS-rank (random values)", 'Min-heap', x, finalTimesOSRankTest)
    saveGraph("os_rank_with_random_values", graphOSRankRandValues)
    graphOSRankRandValuesZoom = drawGraph("OS-rank (random values) zoom", 'Min-heap', x, finalTimesOSRankTest,True)
    saveGraph("os_rank_with_random_values_zoom", graphOSRankRandValuesZoom)




if __name__ == "__main__":
    #prova2()
    runAllTests()

    """x = (10,20,30,40,50)
    y = (4,2,3,1,5)
    y1 = (7,3,5,4,10)
    graph1 = drawGraph("prova funzione", x, y, y1)
    graph1.show()"""



    """
    tempiFinali = []
    n = 20
    for i in range(n):
        #print("-----",i,"-----")
        tempi = []
        tempi.append(searchMaxBSTTest(generateRandomValues(20,1,100)))
        tempi.append(searchMaxBSTTest(generateIncreasingValues(1,20)))
        tempi.append(searchMaxBSTTest(generateDecreasingValues(20,1)))
        tempiFinali.append(tempi)
    print("\n", tempiFinali)
    tempiFinali = np.sum(tempiFinali, axis=0)
    print("\n",tempiFinali)

    print("\n---Valori Finali---\n")
    tempiFinali = np.divide(tempiFinali, n)
    print("\n",tempiFinali)

    
    #prova somma matrice 1
    tempiFinali = []
    for i in range(5):
        # print("-----",i,"-----")
        tempi = []
        tempi.append(i)
        tempi.append(i+1)
        tempi.append(i+2)
        tempiFinali.append(tempi)
    print("\n", tempiFinali)
    tempiFinali = np.sum(tempiFinali, axis=0)
    print("\n",tempiFinali)
    """


    """
    #prova somma matrice 1
    finali= []

    for i in range(5):
        times = []
        for j in range(5):
            times.append(j)
        finali.append(times)
    print(finali)

    finali = np.sum(finali,axis=0)
    print(finali)
    finali = np.divide(finali,5)
    print(finali)"""
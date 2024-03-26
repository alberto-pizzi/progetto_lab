
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
#FIXME
import pandas as pd
import bst_implementation as BST
import lists_implementation as LL
import heap_implementation as HP
import random
import math
import jinja2

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

def saveTable(xValues, timesPerDataStructure, fileName):
    precision = 5
    timesPerDataStructure = timesPerDataStructure.reshape(timesPerDataStructure.shape[0],timesPerDataStructure.shape[2])
    if timesPerDataStructure.shape[1] > 2:
        table = pd.DataFrame(timesPerDataStructure,index=xValues, columns=['Heap', 'Lista non ordinata', 'Lista ordinata'])
    else:
        table = pd.DataFrame(timesPerDataStructure, index=xValues,
                             columns=['Heap', 'Lista ordinata'])

    # Correct precision
    columns = list(table.columns)
    for i in columns:
        table[i] = [np.format_float_scientific(x, precision=precision) for x in table[i]]

    # Save Latex table
    dir = 'Tables/' + fileName + '.tex'
    table.to_latex(dir,index=True)


def drawGraph(graphTitle, labelHeapType, xValues, testFinalTimes,zoom = False):
    # FIXME optimize it
    yHeapValues = []
    yLinkedListValues = []
    ySortredListValues = []
    #testFinalTimes = testFinalTimes.reshape(testFinalTimes.shape[0],testFinalTimes.shape[2])
    for i in range(testFinalTimes.shape[0]):
        yHeapValues.append(testFinalTimes[i,0, 0])
        if testFinalTimes.shape[2] > 2:
            yLinkedListValues.append(testFinalTimes[i,0, 1])
            ySortredListValues.append(testFinalTimes[i, 0, 2])
        else:
            ySortredListValues.append(testFinalTimes[i,0,1])

    graph = plt.figure()
    plt.title(graphTitle)
    if zoom:
        zoomGrade = 13
        maxEl = np.max(testFinalTimes)
        # set zoom scale
        plt.ylim(0,maxEl/zoomGrade)

    plt.xlabel("Numero di elementi")
    plt.ylabel("Tempi (s)")
    plt.plot(xValues, yHeapValues, color='red', label=labelHeapType)
    if testFinalTimes.shape[2] > 2:
        plt.plot(xValues, yLinkedListValues, color='blue', label='Lista non ordinata')
    plt.plot(xValues, ySortredListValues, color='green', label='Lista ordinata')
    plt.legend()
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

def osSelectLLTest(values, iPos):
    newSortedList = LL.LinkedList()
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
    times = []
    for i in range(len(values)):
        timeHeap = searchMinMinHeapTest(values[i])
        timeLL = searchMinLLTest(values[i])
        timeSLL = searchMinSLLTest(values[i])
        times.append([timeHeap, timeLL, timeSLL])
    return times

def oSRankTests(values):

    #randomTarget = values[len(values)-1]
    #print('\nSearching Max in BST test:\n')
    times = []
    for i in range(len(values)):
        randomTarget = random.choice(values[i])
        timeHeap = osRankMinHeapTest(values[i],randomTarget)
        #print('\nSearching Max in Sorted Linked List test:\n')
        timeSLL = osRankSLLTest(values[i],randomTarget)
        times.append([timeHeap, timeSLL])
    return times

def oSSelectTests(values):

    #print('\nSearching Max in BST test:\n')
    times = []
    for i in range(len(values)):
        iPosition = random.randint(1, len(values[i]))
        timeHeap = osSelectMinHeapTest(values[i],iPosition-1)
        #timeLL = osSelectLLTest(values[i],iPosition)
        #print('\nSearching Max in Sorted Linked List test:\n')
        timeSLL = osSelectSLLTest(values[i],iPosition)
        times.append([timeHeap, timeSLL])
    return times

def runAllTests():
    n = 150
    totalDataStructures = 3
    totalValueGenerationWays = 3
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
    finalTimesMaxTest = finalTimesMaxTest.reshape(len(x), totalValueGenerationWays,totalDataStructures)
    finalTimesMinTest = finalTimesMinTest.reshape(len(x), totalValueGenerationWays,totalDataStructures)
    # FIXME
    # sorted data structures are 2
    finalTimesOSSelectTest = finalTimesOSSelectTest.reshape(len(x), totalValueGenerationWays,2)
    finalTimesOSRankTest = finalTimesOSRankTest.reshape(len(x), totalValueGenerationWays,2)

    # Max
    graphMaxRandValues = drawGraph("Cerca Max (random values)",'Max-heap',x,finalTimesMaxTest[:,:1,:])
    saveGraph("max_search_with_random_values",graphMaxRandValues)
    saveTable(x,finalTimesMaxTest[:,:1,:],'max_with_random_values_table')

    graphMaxIncValues = drawGraph("Cerca Max (increasing values)", 'Max-heap', x, finalTimesMaxTest[:, 1:2, :])
    saveGraph("max_search_with_increasing_values", graphMaxIncValues)
    saveTable(x, finalTimesMaxTest[:, 1:2, :], 'max_with_inc_values_table')

    graphMaxDecValues = drawGraph("Cerca Max (decreasing values)", 'Max-heap', x, finalTimesMaxTest[:, 2:, :])
    saveGraph("max_search_with_decreasing_values", graphMaxDecValues)
    saveTable(x, finalTimesMaxTest[:, 2:, :], 'max_with_dec_values_table')



    # Min
    graphMinRandValues = drawGraph("Cerca Min (random values)", 'Min-heap', x, finalTimesMinTest[:,:1,:])
    saveGraph("min_search_with_random_values", graphMinRandValues)
    saveTable(x, finalTimesMinTest[:,:1,:], 'min_with_random_values_table')
    graphMinRandValuesZoom = drawGraph("Cerca Min (random values) zoom", 'Min-heap', x, finalTimesMinTest[:,:1,:],True)
    saveGraph("min_search_with_random_values_zoom", graphMinRandValuesZoom)

    graphMinIncValues = drawGraph("Cerca Min (increasing values)", 'Min-heap', x, finalTimesMinTest[:,1:2,:])
    saveGraph("min_search_with_increasing_values", graphMinIncValues)
    saveTable(x, finalTimesMinTest[:, 1:2, :], 'min_with_inc_values_table')
    graphMinIncValuesZoom = drawGraph("Cerca Min (increasing values) zoom", 'Min-heap', x, finalTimesMinTest[:,1:2,:],True)
    saveGraph("min_search_with_increasing_values_zoom", graphMinIncValuesZoom)

    graphMinDecValues = drawGraph("Cerca Min (decreasing values)", 'Min-heap', x, finalTimesMinTest[:, 2:, :])
    saveGraph("min_search_with_decreasing_values", graphMinDecValues)
    saveTable(x, finalTimesMinTest[:, 2:, :], 'min_with_dec_values_table')
    graphMinDecValuesZoom = drawGraph("Cerca Min (decreasing values) zoom", 'Min-heap', x, finalTimesMinTest[:, 2:, :],
                                      True)
    saveGraph("min_search_with_decreasing_values_zoom", graphMinDecValuesZoom)

    # to free up memory
    plt.close('all')

    # OS-select
    graphOSSelectRandValues = drawGraph("OS-select (random values)", 'Min-heap', x, finalTimesOSSelectTest[:,:1,:])
    saveGraph("os_select_with_random_values", graphOSSelectRandValues)
    saveTable(x, finalTimesOSSelectTest[:, :1, :], 'osselect_with_random_values_table')
    graphOSSelectRandValuesZoom = drawGraph("OS-select (random values) zoom", 'Min-heap', x, finalTimesOSSelectTest[:,:1,:],True)
    saveGraph("os_select_with_random_values_zoom", graphOSSelectRandValuesZoom)


    graphOSSelectIncValues = drawGraph("OS-select (increasing values)", 'Min-heap', x, finalTimesOSSelectTest[:,1:2,:])
    saveGraph("os_select_with_increasing_values", graphOSSelectIncValues)
    saveTable(x, finalTimesOSSelectTest[:, 1:2, :], 'osselect_with_inc_values_table')
    graphOSSelectIncValuesZoom = drawGraph("OS-select (increasing values) zoom", 'Min-heap', x, finalTimesOSSelectTest[:,1:2,:],
                                            True)
    saveGraph("os_select_with_increasing_values_zoom", graphOSSelectIncValuesZoom)


    graphOSSelectDecValues = drawGraph("OS-select (decreasing values)", 'Min-heap', x,
                                       finalTimesOSSelectTest[:, 2:, :])
    saveGraph("os_select_with_decreasing_values", graphOSSelectDecValues)
    saveTable(x, finalTimesOSSelectTest[:, 2:, :], 'osselect_with_dec_values_table')
    graphOSSelectDecValuesZoom = drawGraph("OS-select (decreasing values) zoom", 'Min-heap', x,
                                           finalTimesOSSelectTest[:, 2:, :],
                                           True)
    saveGraph("os_select_with_decreasing_values_zoom", graphOSSelectDecValuesZoom)


    #OS-rank
    graphOSRankRandValues = drawGraph("OS-rank (random values)", 'Min-heap', x, finalTimesOSRankTest[:,:1,:])
    saveGraph("os_rank_with_random_values", graphOSRankRandValues)
    saveTable(x, finalTimesOSRankTest[:, :1, :], 'osrank_with_random_values_table')
    graphOSRankRandValuesZoom = drawGraph("OS-rank (random values) zoom", 'Min-heap', x, finalTimesOSRankTest[:,:1,:],True)
    saveGraph("os_rank_with_random_values_zoom", graphOSRankRandValuesZoom)

    graphOSRankIncValues = drawGraph("OS-rank (increasing values)", 'Min-heap', x, finalTimesOSRankTest[:,1:2,:])
    saveGraph("os_rank_with_increasing_values", graphOSRankIncValues)
    saveTable(x, finalTimesOSSelectTest[:, 1:2, :], 'ossrank_with_inc_values_table')
    graphOSRankIncValuesZoom = drawGraph("OS-rank (increasing values) zoom", 'Min-heap', x, finalTimesOSRankTest[:,1:2,:], True)
    saveGraph("os_rank_with_increasing_values_zoom", graphOSRankIncValuesZoom)

    graphOSRankDecValues = drawGraph("OS-rank (decreasing values)", 'Min-heap', x, finalTimesOSRankTest[:, 2:, :])
    saveGraph("os_rank_with_decreasing_values", graphOSRankDecValues)
    saveTable(x, finalTimesOSRankTest[:, 2:, :], 'osrank_with_dec_values_table')
    graphOSRankDecValuesZoom = drawGraph("OS-rank (decreasing values) zoom", 'Min-heap', x,
                                         finalTimesOSRankTest[:, 2:, :], True)
    saveGraph("os_rank_with_decreasing_values_zoom", graphOSRankDecValuesZoom)




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
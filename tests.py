
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import pandas as pd
import lists_implementation as LL
import heap_implementation as HP
import random
import math
import jinja2

def generateRandomValues(totalValues, minRandomValue, maxRandomValue):
    randomValues = []
    for i in range(totalValues):
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


def searchMinMinHeapTest(values):
    # Create Min-heap with input values
    newHeap = HP.Minheap()
    newHeap.buildHeap(values)
    start = timer()
    minBST = newHeap.minimum()
    end = timer()
    time = end-start
    return time

def searchMinMaxHeapTest(values):
    # Create Max-heap with input values
    newHeap = HP.Maxheap()
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

def searchMaxMinHeapTest(values):
    # Create Min-heap with input values
    newHeap = HP.Minheap()
    newHeap.buildHeap(values)
    start = timer()
    minBST = newHeap.maximum()
    end = timer()
    time = end-start
    return time


def osRankMinHeapTest(values, targetValue):
    # Create Min-heap with input values
    newHeap = HP.Minheap()

    newHeap.buildHeap(values)

    start = timer()
    rank = newHeap.osRank(targetValue)
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

def createAndSaveTable(xValues, timesPerDataStructure, fileName):
    precision = 5
    timesPerDataStructure = timesPerDataStructure.reshape(timesPerDataStructure.shape[0],timesPerDataStructure.shape[2])
    if timesPerDataStructure.shape[1] > 3:
        table = pd.DataFrame(timesPerDataStructure,index=xValues, columns=['Min-Heap', 'Lista non ordinata', 'Lista ordinata','Max-Heap'])
    else:
        table = pd.DataFrame(timesPerDataStructure, index=xValues,
                             columns=['Min-heap', 'Lista ordinata', 'Lista non ordinata'])

    # Correct precision
    columns = list(table.columns)
    for i in columns:
        table[i] = [np.format_float_scientific(x, precision=precision) for x in table[i]]

    # Save Latex table
    dir = 'Tables/' + fileName + '.tex'
    table.to_latex(dir,index=True)


def drawGraph(graphTitle, xValues, testFinalTimes, zoom=False,zoomGrade=20):
    yMaxHeapValues = []
    yLinkedListValues = []
    ySortredListValues = []
    yMinHeapValues = []
    #testFinalTimes = testFinalTimes.reshape(testFinalTimes.shape[0],testFinalTimes.shape[2])
    for i in range(testFinalTimes.shape[0]):
        yMinHeapValues.append(testFinalTimes[i, 0, 0])
        if testFinalTimes.shape[2] > 3:
            yLinkedListValues.append(testFinalTimes[i,0, 1])
            ySortredListValues.append(testFinalTimes[i, 0, 2])
            yMaxHeapValues.append(testFinalTimes[i, 0, 3])
        else:
            ySortredListValues.append(testFinalTimes[i,0,1])
            yLinkedListValues.append(testFinalTimes[i, 0, 2])


    graph = plt.figure()

    if zoom:
        title = graphTitle + ' ' + str(zoomGrade) + 'x'
        maxEl = np.max(testFinalTimes)
        # set zoom scale
        plt.ylim(0,maxEl/zoomGrade)
    else:
        title = graphTitle

    plt.title(title)
    plt.xlabel("Numero di elementi")
    plt.ylabel("Tempi (s)")

    plt.plot(xValues, yMinHeapValues, color='red', label='Min-heap')
    if testFinalTimes.shape[2] > 3:
        plt.plot(xValues, yMaxHeapValues, color='pink', label='Max-heap')
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

def osRankLLTest(values, targetValue):
    newList = LL.LinkedList()
    for i in values:
        newList.addElement(i)

    start = timer()
    rank = newList.osRank(targetValue)
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
    newList = LL.LinkedList()
    for i in values:
        newList.addElement(i)

    start = timer()
    rank = newList.osSelect(iPos)
    end = timer()
    time = end-start
    return time

def searchMaxTests(values):
    times = []
    for i in range(len(values)):
        timeMaxHeap = searchMaxMaxHeapTest(values[i])
        timeMinHeap = searchMaxMinHeapTest(values[i])
        timeSLL = searchMaxSLLTest(values[i])
        timeLL = searchMaxLLTest(values[i])
        times.append([timeMinHeap, timeLL, timeSLL, timeMaxHeap])
    return times
def searchMinTests(values):
    times = []
    for i in range(len(values)):
        timeMinHeap = searchMinMinHeapTest(values[i])
        timeMaxHeap = searchMinMaxHeapTest(values[i])
        timeLL = searchMinLLTest(values[i])
        timeSLL = searchMinSLLTest(values[i])
        times.append([timeMinHeap, timeLL, timeSLL, timeMaxHeap])
    return times

def oSRankTests(values):
    times = []
    for i in range(len(values)):
        randomTarget = random.choice(values[i])
        timeMinHeap = osRankMinHeapTest(values[i],randomTarget)
        timeSLL = osRankSLLTest(values[i],randomTarget)
        timeLL = osRankLLTest(values[i],randomTarget)
        times.append([timeMinHeap, timeSLL,timeLL])
    return times

def oSSelectTests(values):
    times = []
    for i in range(len(values)):
        iPosition = random.randint(1, len(values[i]))
        timeMinHeap = osSelectMinHeapTest(values[i],iPosition-1)
        timeSLL = osSelectSLLTest(values[i],iPosition)
        timeLL = osSelectLLTest(values[i],iPosition)
        times.append([timeMinHeap, timeSLL,timeLL])
    return times

def runAllTests():

    nIterations = 150
    # Heap (general), LL, SLL
    totalDataStructures = 3
    # Rand, inc , dec
    totalValueGenerationWays = 3
    #x = [g for g in range(50,500,50)]
    x = [50,250,500,1000,5000,12000]
    finalTimesMaxTest = np.array([])
    finalTimesMinTest = np.array([])
    finalTimesOSSelectTest = np.array([])
    finalTimesOSRankTest = np.array([])
    for j in x:
        timesMaxTests = []
        timesMinTests = []
        timesOSSelectTests = []
        timesOSRankTests = []
        for i in range(nIterations):
            values = []
            values.append(generateRandomValues(j, 1, 10000))
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

        # Calculate averages:

        # Maximum
        timesMaxTests = np.sum(timesMaxTests, axis=0)
        timesMaxTests = np.divide(timesMaxTests, nIterations)
        finalTimesMaxTest = np.append(finalTimesMaxTest, timesMaxTests)
        # Minimum
        timesMinTests = np.sum(timesMinTests, axis=0)
        timesMinTests = np.divide(timesMinTests, nIterations)
        finalTimesMinTest = np.append(finalTimesMinTest, timesMinTests)
        # OS-Select
        timesOSSelectTests = np.sum(timesOSSelectTests, axis=0)
        timesOSSelectTests = np.divide(timesOSSelectTests, nIterations)
        finalTimesOSSelectTest = np.append(finalTimesOSSelectTest, timesOSSelectTests)
        # OS-Rank
        timesOSRankTests = np.sum(timesOSRankTests, axis=0)
        timesOSRankTests = np.divide(timesOSRankTests, nIterations)
        finalTimesOSRankTest = np.append(finalTimesOSRankTest, timesOSRankTests)

    # Reshape matrix:

    # Data structures with max and min comparing are 4: max-heap, min-heap, LL and SLL
    finalTimesMaxTest = finalTimesMaxTest.reshape(len(x), totalValueGenerationWays,totalDataStructures+1)
    finalTimesMinTest = finalTimesMinTest.reshape(len(x), totalValueGenerationWays,totalDataStructures+1)
    # Sorted data structures are 2: min-heap and SLL
    finalTimesOSSelectTest = finalTimesOSSelectTest.reshape(len(x), totalValueGenerationWays,totalDataStructures)
    finalTimesOSRankTest = finalTimesOSRankTest.reshape(len(x), totalValueGenerationWays,totalDataStructures)

    # Max
    graphMaxRandValues = drawGraph("Cerca Max (valori random)", x, finalTimesMaxTest[:, :1, :])
    saveGraph("max_search_with_random_values",graphMaxRandValues)
    createAndSaveTable(x, finalTimesMaxTest[:, :1, :], 'max_with_random_values_table')

    graphMaxIncValues = drawGraph("Cerca Max (valori crescenti)", x, finalTimesMaxTest[:, 1:2, :])
    saveGraph("max_search_with_increasing_values", graphMaxIncValues)
    createAndSaveTable(x, finalTimesMaxTest[:, 1:2, :], 'max_with_inc_values_table')

    graphMaxDecValues = drawGraph("Cerca Max (valori decrescenti)", x, finalTimesMaxTest[:, 2:, :])
    saveGraph("max_search_with_decreasing_values", graphMaxDecValues)
    createAndSaveTable(x, finalTimesMaxTest[:, 2:3, :], 'max_with_dec_values_table')

    # Min
    graphMinRandValues = drawGraph("Cerca Min (valori random)", x, finalTimesMinTest[:,:1,:])
    saveGraph("min_search_with_random_values", graphMinRandValues)
    createAndSaveTable(x, finalTimesMinTest[:, :1, :], 'min_with_random_values_table')
    graphMinRandValuesZoom = drawGraph("Cerca Min (valori random) zoom",  x, finalTimesMinTest[:,:1,:],True)
    saveGraph("min_search_with_random_values_zoom", graphMinRandValuesZoom)

    graphMinIncValues = drawGraph("Cerca Min (valori crescenti)",  x, finalTimesMinTest[:,1:2,:])
    saveGraph("min_search_with_increasing_values", graphMinIncValues)
    createAndSaveTable(x, finalTimesMinTest[:, 1:2, :], 'min_with_inc_values_table')
    graphMinIncValuesZoom = drawGraph("Cerca Min (valori crescenti) zoom",  x, finalTimesMinTest[:,1:2,:],True)
    saveGraph("min_search_with_increasing_values_zoom", graphMinIncValuesZoom)

    graphMinDecValues = drawGraph("Cerca Min (valori decrescenti)", x, finalTimesMinTest[:, 2:, :])
    saveGraph("min_search_with_decreasing_values", graphMinDecValues)
    createAndSaveTable(x, finalTimesMinTest[:, 2:, :], 'min_with_dec_values_table')
    graphMinDecValuesZoom = drawGraph("Cerca Min (valori decrescenti) zoom", x, finalTimesMinTest[:, 2:, :],
                                      True)
    saveGraph("min_search_with_decreasing_values_zoom", graphMinDecValuesZoom)

    # to free up memory
    plt.close('all')

    # OS-select
    zoom = 1000
    graphOSSelectRandValues = drawGraph("OS-select (valori random)",  x, finalTimesOSSelectTest[:,:1,:])
    saveGraph("os_select_with_random_values", graphOSSelectRandValues)
    createAndSaveTable(x, finalTimesOSSelectTest[:, :1, :], 'osselect_with_random_values_table')
    graphOSSelectRandValuesZoom20 = drawGraph("OS-select (valori random) zoom",  x, finalTimesOSSelectTest[:,:1,:],True)
    saveGraph("os_select_with_random_values_zoom", graphOSSelectRandValuesZoom20)
    graphOSSelectRandValuesZoom100 = drawGraph("OS-select (valori random) zoom", x, finalTimesOSSelectTest[:, :1, :],
                                              True,zoom)
    saveGraph("os_select_with_random_values_zoom_100", graphOSSelectRandValuesZoom100)


    graphOSSelectIncValues = drawGraph("OS-select (valori crescenti)",  x, finalTimesOSSelectTest[:,1:2,:])
    saveGraph("os_select_with_increasing_values", graphOSSelectIncValues)
    createAndSaveTable(x, finalTimesOSSelectTest[:, 1:2, :], 'osselect_with_inc_values_table')
    graphOSSelectIncValuesZoom20 = drawGraph("OS-select (valori crescenti) zoom",  x, finalTimesOSSelectTest[:,1:2,:],
                                            True)
    saveGraph("os_select_with_increasing_values_zoom", graphOSSelectIncValuesZoom20)
    graphOSSelectIncValuesZoom100 = drawGraph("OS-select (valori crescenti) zoom", x, finalTimesOSSelectTest[:, 1:2, :],
                                             True,zoom)
    saveGraph("os_select_with_increasing_values_zoom_100", graphOSSelectIncValuesZoom100)


    graphOSSelectDecValues = drawGraph("OS-select (valori decrescenti)",  x,
                                       finalTimesOSSelectTest[:, 2:, :])
    saveGraph("os_select_with_decreasing_values", graphOSSelectDecValues)
    createAndSaveTable(x, finalTimesOSSelectTest[:, 2:, :], 'osselect_with_dec_values_table')
    graphOSSelectDecValuesZoom20 = drawGraph("OS-select (valori decrescenti) zoom",  x,
                                           finalTimesOSSelectTest[:, 2:, :],
                                           True)
    saveGraph("os_select_with_decreasing_values_zoom", graphOSSelectDecValuesZoom20)
    graphOSSelectDecValuesZoom100 = drawGraph("OS-select (valori decrescenti) zoom", x,
                                           finalTimesOSSelectTest[:, 2:, :],
                                           True,zoom)
    saveGraph("os_select_with_decreasing_values_zoom_100", graphOSSelectDecValuesZoom100)


    #OS-rank

    graphOSRankRandValues = drawGraph("OS-rank (valori random)",  x, finalTimesOSRankTest[:,:1,:])
    saveGraph("os_rank_with_random_values", graphOSRankRandValues)
    createAndSaveTable(x, finalTimesOSRankTest[:, :1, :], 'osrank_with_random_values_table')
    graphOSRankRandValuesZoom20 = drawGraph("OS-rank (valori random) zoom", x, finalTimesOSRankTest[:,:1,:],True)
    saveGraph("os_rank_with_random_values_zoom", graphOSRankRandValuesZoom20)
    graphOSRankRandValuesZoom100 = drawGraph("OS-rank (valori random) zoom", x, finalTimesOSRankTest[:, :1, :], True,zoom)
    saveGraph("os_rank_with_random_values_zoom_100", graphOSRankRandValuesZoom100)

    graphOSRankIncValues = drawGraph("OS-rank (valori crescenti)",  x, finalTimesOSRankTest[:,1:2,:])
    saveGraph("os_rank_with_increasing_values", graphOSRankIncValues)
    createAndSaveTable(x, finalTimesOSSelectTest[:, 1:2, :], 'ossrank_with_inc_values_table')
    graphOSRankIncValuesZoom20 = drawGraph("OS-rank (valori crescenti) zoom",  x, finalTimesOSRankTest[:,1:2,:], True)
    saveGraph("os_rank_with_increasing_values_zoom", graphOSRankIncValuesZoom20)
    graphOSRankIncValuesZoom100 = drawGraph("OS-rank (valori crescenti) zoom", x, finalTimesOSRankTest[:, 1:2, :], True,zoom)
    saveGraph("os_rank_with_increasing_values_zoom_100", graphOSRankIncValuesZoom100)

    graphOSRankDecValues = drawGraph("OS-rank (valori decrescenti)",  x, finalTimesOSRankTest[:, 2:, :])
    saveGraph("os_rank_with_decreasing_values", graphOSRankDecValues)
    createAndSaveTable(x, finalTimesOSRankTest[:, 2:, :], 'osrank_with_dec_values_table')
    graphOSRankDecValuesZoom20 = drawGraph("OS-rank (valori decrescenti) zoom",  x,
                                         finalTimesOSRankTest[:, 2:, :], True)
    saveGraph("os_rank_with_decreasing_values_zoom", graphOSRankDecValuesZoom20)
    graphOSRankDecValuesZoom100 = drawGraph("OS-rank (valori decrescenti) zoom", x,
                                         finalTimesOSRankTest[:, 2:, :], True,zoom)
    saveGraph("os_rank_with_decreasing_values_zoom_100", graphOSRankDecValuesZoom100)





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
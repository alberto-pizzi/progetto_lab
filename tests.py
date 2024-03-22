
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import bst_implementation as BST
import lists_implementation as LL
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

def drawGraph(graphTitle, xValues, yBstValues, yLinkedListValues):
    # FIXME
    graph = plt.figure()
    plt.title(graphTitle)
   #fig,ax=plt.subplots()
    ultimoEl = np.max(yBstValues)
    #plt.ylim(0,ultimoEl*3)
    plt.ylim(0, 0.001)
    #plt.xlim(0,500)
    #ylog= np.log2(rif)
    plt.xlabel("Numero di elementi")
    plt.ylabel("Tempi")
    plt.plot(xValues, yBstValues, color='red', label='ABR')
    plt.plot(xValues, yLinkedListValues, color='blue', label='Lista Ordinata')
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

def searchMinSLLTest(values):
    newSortedList = LL.SortedLinkedList()
    for i in values:
        newSortedList.addElement(i)

    start = timer()
    minSLL = newSortedList.minElement()
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
    #print('\nSearching Max in BST test:\n')
    timeBST = searchMaxBSTTest(values)
    #print('\nSearching Max in Sorted Linked List test:\n')
    timeSLL = searchMaxSLLTest(values)
    times = [timeBST, timeSLL]
    return times
def searchMinTests(values):
    #print('\nSearching Max in BST test:\n')
    timeBST = searchMinBSTTest(values)
    #print('\nSearching Max in Sorted Linked List test:\n')
    timeSLL = searchMinSLLTest(values)
    times = [timeBST, timeSLL]
    return times

def oSRankTests(values):
    randomTarget = random.choice(values)
    #print('\nSearching Max in BST test:\n')
    timeBST = osRankBSTTest(values,randomTarget)
    #print('\nSearching Max in Sorted Linked List test:\n')
    timeSLL = osRankSLLTest(values,randomTarget)
    times = [timeBST, timeSLL]
    return times

def oSSelectTests(values):
    iPosition = random.randint(1,len(values))
    #print('\nSearching Max in BST test:\n')
    timeBST = osRankBSTTest(values,iPosition)
    #print('\nSearching Max in Sorted Linked List test:\n')
    timeSLL = osRankSLLTest(values,iPosition)
    times = [timeBST, timeSLL]
    return times

def runAllTests():
    # FIXME
    n = 100
    #x = [g for g in range(200,2000,200)]
    x = [50,250,500,1000,5000,10000]
    finalTimes = np.array([])
    for j in x:
        timesMaxTests = []
        for i in range(n):
            values = []
            #values = generateRandomValues(0,j,1,10000)
            values = generateDecreasingValues(j,1)
            print("\nTest: ",i+1,"with ",j," elements")
            timesMaxTest = oSRankTests(values)
            timesMaxTests.append(timesMaxTest)
        timesMaxTests = np.sum(timesMaxTests, axis=0)
        timesMaxTests = np.divide(timesMaxTests, n)
        finalTimes = np.append(finalTimes, timesMaxTests)

    finalTimes = finalTimes.reshape(len(x), 2)
    print("\nfinalTimes:\n",finalTimes)
    finalTimesBST = finalTimes[:, :1]
    finalTimesSLL = finalTimes[:, 1:]
    print("\n Tempi BST:",finalTimesBST)
    print("\n Tempi SLL:", finalTimesSLL)
    graph = drawGraph("OS Rank",x,finalTimesBST,finalTimesSLL)
    graph.show()


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
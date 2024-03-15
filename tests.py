
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import bst_implementation as BST
import random

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

#FIXME verificare se serve il tempo medio (vidivendo per la lunghezza della lista)
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
    return (time/len(values))

def drawGraph(graphTitle, xValues, yBstValues, yLinkedListValues):
    graph = plt.figure()
    plt.title(graphTitle)
    plt.xlabel("Numero di elementi")
    plt.ylabel("Tempi")
    plt.plot(xValues, yBstValues, color='red', label='ABR')
    plt.plot(xValues, yLinkedListValues, color='blue', label='Lista Ordinata')
    plt.legend()
    return graph




if __name__ == "__main__":
    #prova2()

    x = (10,20,30,40,50)
    y = (4,2,3,1,5)
    y1 = (7,3,5,4,10)
    graph = drawGraph("prova funzione", x, y, y1)
    graph.show()

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
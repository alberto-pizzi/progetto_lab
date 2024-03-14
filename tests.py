
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import bst_implementation as BST
import random

#TODO da rimuovere
def prova():
    # Seno e coseno
    x = np.arange(0, 3 * np.pi, 0.1)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    # usiamo matplotlib
    plt.plot(x, y_sin)
    plt.plot(x, y_cos)
    plt.xlabel("x axis label")
    plt.ylabel("y axis label")
    plt.title("Sine and Cosine")
    plt.legend(["Sine", "Cosine"])
    #plt.savefig("prova.png")
    plt.show()

def prova2():
    x = (10,20,30,40,50)
    y = (4,2,3,1,5)
    # usiamo matplotlib
    plt.plot(x, y)
    plt.xlabel("x axis label")
    plt.ylabel("y axis label")
    plt.title("Prova nuova")
    plt.legend(["Primo"])
    #plt.savefig("prova.png")
    plt.show()

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
    newBST.inorderTraversal(newBST.root)
    print("\n")
    start = timer()
    maxBST = newBST.nodeMaximum(newBST.root).value
    end = timer()
    time = end - start
    return (time),maxBST


if __name__ == "__main__":
    #prova2()
    print("time random: ",searchMaxBSTTest(generateRandomValues(20,1,100)))
    print("\ntime: ",searchMaxBSTTest(generateIncreasingValues(1,20)))
    print("\ntime: ",searchMaxBSTTest(generateDecreasingValues(20,1)))

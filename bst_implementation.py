import numpy as np
import random
import sys
sys.setrecursionlimit(10**9)
class BSTNode:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
        self.parent = None

class BSTree:
    def __init__(self):
        self.root = None

    def inorderTraversal(self,root):
        if root is not None:
            self.inorderTraversal(root.left)
            print(root.value, end=' ')
            self.inorderTraversal(root.right)

    # TODO remove
    def calculateSize(self, subRoot):
        if subRoot is not None:
            left_child_count = self.calculateSize(subRoot.left)  # Attraversa il sottoalbero sinistro
            right_child_count = self.calculateSize(subRoot.right)  # Attraversa il sottoalbero destro
            total_children = left_child_count + right_child_count  # Somma il numero di figli
            return total_children + 1  # Restituisce il numero totale di figli (incluse radice e foglie)
        else:
            return 0  # Se il nodo è None, non ha figli

    # TODO rimuovere se non serve
    def preorderTraversal(self, root):
        if root is not None:
            print(root.value, end=' ')
            self.inorderTraversal(root.left)
            self.inorderTraversal(root.right)

    # TODO rimuovere se non serve
    def postorderTraversal(self, root):
        if root is not None:
            self.inorderTraversal(root.left)
            self.inorderTraversal(root.right)
            print(root.value, end=' ')

    def sortedArrayToBalancedTree(self, a):
        if not a:
            return None
        mid = len(a) // 2
        root = BSTNode(a[mid])
        root.left = self.sortedArrayToBalancedTree(a[:mid])
        root.right = self.sortedArrayToBalancedTree(a[mid + 1:])
        return root


    def height(self, node):
        if node is None:
            return 0
        left = self.height(node.left)
        right = self.height(node.right)
        return max(left, right) + 1

    def insertElement(self,value):
        newNode = BSTNode(value)
        if self.root is None:
            self.root = newNode
            return
        prev = None
        tmp = self.root
        while tmp is not None:
            prev = tmp
            if (value < tmp.value):
                tmp = tmp.left
            else:
                tmp = tmp.right
        newNode.parent = prev
        if (value < prev.value):
            prev.left = newNode
        else:
            prev.right = newNode

    # TODO remove if not useful
    def searchValue(self, value):
        currentNode = self.root
        while currentNode is not None:
            if currentNode.value == value:
                return True
            elif value < currentNode.value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return False

    def searchNode(self,value):
        currentNode = self.root
        while currentNode is not None and value != currentNode.value:
            if value < currentNode.value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return currentNode

    def nodeMinimum(self, node):
        currentNode = node
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode

    def nodeMaximum(self, node):
        currentNode = node
        while currentNode.right is not None:
            currentNode = currentNode.right
        return currentNode

    # TODO rimuovere se non serve
    def nodeSuccessor(self, node):
        currentNode = node
        if currentNode.right is not None:
            return self.nodeMinimum(currentNode.right)
        prev = currentNode.parent
        while prev is not None and currentNode is prev.right:
            currentNode = prev
            prev = prev.parent
        return prev

    def nodePredecessor(self, node):
        currentNode = node
        if currentNode.left is not None:
            return self.nodeMaximum(currentNode.left)
        prev = currentNode.parent
        while prev is not None and currentNode is prev.left:
            currentNode = prev
            prev = prev.parent
        return prev

    # TODO rimuovere se non serve
    def transplant(self, oldRootNode, newRootNode):
        if oldRootNode.parent is None:
            self.root = newRootNode
        elif oldRootNode is oldRootNode.parent.left:
            oldRootNode.parent.left = newRootNode
        else:
            oldRootNode.parent.right = newRootNode
        if newRootNode is not None:
            newRootNode.parent = oldRootNode.parent

    # TODO rimuovere se non serve
    def deleteNode(self, node):
        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            y = self.nodeMinimum(node.right)
            if y.parent is not node:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y

    # TODO rimuovere se non serve
    # Finds k-th smallest value
    def osSelectSmallest(self,root,k):
        currentNode = self.nodeMinimum(root)
        for i in range(k-1):
            if currentNode is None:
                return None
            currentNode = self.nodeSuccessor(currentNode)

        return currentNode.value

    # TODO rimuovere se non serve
    # Finds k-th biggest value
    def osSelectBiggest(self,root,k):
        currentNode = self.nodeMaximum(root)
        for i in range(k-1):
            if currentNode is None:
                return None
            currentNode = self.nodePredecessor(currentNode)

        return currentNode.value

    # TODO rimuovere se non si usa
    def size(self,root):
        if root is None:
            return 0
        else:
            return self.size(root.left)+self.size(root.right)+1

    """
    def osRank(self,root,target):
        if root is None:
            return 0
        if target < root.value:
            return self.osRank(root.left, target)
        elif target > root.value:
            return 1 + self.size(root.left) + self.osRank(root.right, target)
        else:
            return self.size(root.left) + 1
    # TODO vedre quali delle due implementazioni è la migliore
    # FIXME per i valori non presente restituisce il rango più alto, invece di None
    def osRank(self,root,target):
        if root is None:
            return 0

        rankLeft = self.osRank(root.left,target)
        rankRight = self.osRank(root.right,target)

        if root.value <= target:
            return 1 + rankLeft + rankRight
        else:
            return rankLeft + rankRight

    # FIXME per i valori non presente restituisce il rango più alto, invece di None
    def osRank(self, target):
        if target is None:
            return 0
        successor = self.nodeSuccessor(self.treeMinimum(self.root))
        rank = 1
        while successor is not None and successor.value <= target.value:
            rank += 1
            successor = self.nodeSuccessor(successor)
        return rank
"""

    # Returns a node (pointer) with i-th smallest value, from a node
    def osSelect(self, subRoot, i):
        rank = self.size(subRoot.left) + 1
        if i == rank:
            return subRoot
        elif i < rank:
            return self.osSelect(subRoot.left, i)
        else:
            return self.osSelect(subRoot.right, i - rank)

    # Returns the rank (number) of node
    def osRank(self, node):
        # FIXME caso: valore non presente
        if node is None:
            return 0
        rank = self.size(node.left) + 1
        y = node
        while y != self.root:
            if y == y.parent.right:
                rank += self.size(y.parent.left) + 1
            y = y.parent
        return rank

    # Returns median value of BST
    def median(self):
        totalNodes = self.size(self.root)
        if totalNodes % 2 == 0:
            mid1 = totalNodes // 2
            mid2 = mid1 + 1
            return (self.osSelect(self.root, mid1).value + self.osSelect(self.root, mid2).value) / 2
        else:
            mid = (totalNodes + 1) // 2
            return self.osSelect(self.root, mid).value
    def testMinSearching(self,expectedValue):
        if (self.nodeMinimum(self.root).value == expectedValue):
            print("\nMin finding is right. Min is ", expectedValue)
        else:
            print("\nMin finding is wrong")
    def testMaxSearching(self,expectedValue):
        if (self.nodeMaximum(self.root).value == expectedValue):
            print("\nMax finding is right. Min is ", expectedValue)
        else:
            print("\nMax finding is wrong")

    def testMedian(self,valueExpected):
        if self.median() == valueExpected:
            print("Median expected is right, that is", valueExpected)
        else:
            print("Median expected is wrong")
    def testOSSelect(self,inputOSSelect,valueExpected):
        if self.osSelect(self.root,inputOSSelect).value == valueExpected:
            print("The result is right, that is", valueExpected)
        else:
            print("The result is wrong")
    def testOSRank(self, inputOSRank, valueExpected):
        if self.osRank(inputOSRank) == valueExpected:
            print("The result (rank) is right, that is", valueExpected)
        else:
            print("The result (rank) is wrong")


def testBST():
    print("\n--------BST test--------\n")
    bst = BSTree()
    for i in range(random.randint(20, 100)):
        bst.insertElement(random.randint(0, 1000))
    print("\n--Inorder traversal--\n")
    bst.inorderTraversal(bst.root)

    # TODO rimuovere questi test e i metodi che non sono necessari per i veir test

    print("\n--Child nodes test--\n")
    if bst.size(bst.root) >= 3:
        if bst.root.value > bst.root.left.value and bst.root.value <= bst.root.right.value:
            print("Correct comparing, Parent > Left Child and Parent <= Right Child")
        else:
            print("Wrong comparing")


    print("\n--Insert test--\n")
    currentTotalNodes = bst.size(bst.root)
    bst.insertElement(40)
    if bst.size(bst.root) == (currentTotalNodes + 1):
        print("Correct insert")
    else:
        print("Wrong insert")

    print("\n--Delete test--\n")
    bst.deleteNode(bst.searchNode(40))
    if bst.size(bst.root) == (currentTotalNodes - 1):
        print("Correct delete")
    else:
        print("Wrong delete")

def testOSBST():
    # Tests OS implementations with specific BST
    print("\n--------OS test for BST--------\n")
    bst = BSTree()

    # Test values
    maxElement = 80
    minElement = 20

    for i in range(random.randint(20, 50)):
        bst.insertElement(random.randint(minElement+1, maxElement-1))
    bst.insertElement(minElement)
    bst.insertElement(maxElement)

    print("\n--Inorder traversal--\n")
    bst.inorderTraversal(bst.root)

    bst.testMaxSearching(maxElement)
    bst.testMinSearching(minElement)


    # Test values
    medianExpectedFromEven = 45
    medianExpectedFromOdd = 50
    medianNotExpected = 100

    bst2 = BSTree()

    bst2.insertElement(50)
    bst2.insertElement(30)
    bst2.insertElement(20)
    bst2.insertElement(40)
    bst2.insertElement(70)
    bst2.insertElement(60)

    print("\n--Inorder traversal--\n")
    bst2.inorderTraversal(bst2.root)

    print("\nTests median from even nodes BST:")
    bst2.testMedian(medianExpectedFromEven)
    bst2.insertElement(80)
    print("\n--Inorder traversal with new element, now we have odd number of nodes--\n")
    bst2.inorderTraversal(bst2.root)
    print("\nTests median from odd nodes BST:")
    bst2.testMedian(medianExpectedFromOdd)
    print("\nTests median from odd nodes BST with UNEXPECTED value:")
    bst2.testMedian(medianNotExpected)


    # Test values

    # Tests OS-select
    inputOSSelect = 3
    expectedValue = 40
    notExpectedValue = 2*expectedValue

    print("\nTest OS-select with expected value (",expectedValue,") from BST:")
    bst2.testOSSelect(inputOSSelect, expectedValue)
    print("\nTest OS-select with NOT expected value (",notExpectedValue,") from BST:")
    bst2.testOSSelect(inputOSSelect, notExpectedValue)

    # Tests OS-rank (return position, rank, of value)

    inputOSRank = bst2.searchNode(40)
    expectedRank = 3
    notExpectedRank = 2*expectedRank

    print("\nTest OS-rank with expected value (",expectedRank, ") from sorted linked list:")
    bst2.testOSRank(inputOSRank, expectedRank)
    print("\nTest OS-rank with NOT expected value (",notExpectedRank,") from sorted linked list:")
    bst2.testOSRank(inputOSRank, notExpectedRank)



#albero = BST()
"""
albero.insertElement(50)
albero.insertElement(30)
albero.insertElement(20)
albero.insertElement(40)
albero.insertElement(70)
albero.insertElement(60)
albero.insertElement(80)

albero.inorderTraversal(albero.root)
print("\n Preorder: ")
albero.preorderTraversal(albero.root)
print("\n Postorder: ")
albero.postorderTraversal(albero.root)
print("\n")
print("60 è nel bst?", albero.searchValue(60))
print("il max è: ", albero.treeMaximum(albero.root).value)
print("il min è: ", albero.treeMinimum(albero.root).value)

print("\nil predecessore di 40: ", albero.nodePredecessor(albero.searchNode(40)).value)

array1 = np.arange(0, 100, 13)
# np.random.shuffle(array1)
for value in array1:
    albero.insertElement(value)
#albero.insertElement(39)
albero.inorderTraversal(albero.root)
print("\nil 4 valore più piccolo è ", albero.osSelect(albero.root,4).value)


print("\nil rango di 39 è: ", albero.osRank(albero.searchNode(39)))
print("size di 0:", albero.size(albero.searchNode(39)))
print("trova mediana:",albero.median())
#print("nodo 40 :",albero.searchNode(40).value)
#albero.treeDelete(albero.searchNode(40))
#albero.inorderTraversal(albero.root)
"""
if __name__ == "__main__":
    #testBST()
    #testOSBST()

    # TODO abilitare i test

    albero = BSTree()

    albero.insertElement(50)
    albero.insertElement(30)
    albero.insertElement(20)
    albero.insertElement(40)
    albero.insertElement(70)
    albero.insertElement(60)
    albero.insertElement(80)

    #albero.inorderTraversal(albero.root)

    print("size: ",albero.calculateSize(albero.root.left))
    print("size 50: ",albero.size(albero.searchNode(50)))
    """
    alt = albero.height(albero.root)
    print("\naltezza: ", alt)
    #array1 = np.arange(0, 1000, 13)
    
    array1 = [i for i in range(100,0,-1)]
    #np.random.shuffle(array1)

    albero = BSTree()
    c=0
    for value in array1:
        albero.insertElement(value)
        c += 1

    #alt = albero.altezza(albero.root)
    print("\ncontatore: ",c)
    print("\naltezza: ", alt)
    #albero.inorderTraversal(albero.root)"""

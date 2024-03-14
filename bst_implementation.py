class BSTNode:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
        self.parent = None

class BST:
    def __init__(self):
        self.root = None

    def inorderTraversal(self,root):
        if root is not None:
            self.inorderTraversal(root.left)
            print(root.value, end=' ')
            self.inorderTraversal(root.right)

    def preorderTraversal(self, root):
        if root is not None:
            print(root.value, end=' ')
            self.inorderTraversal(root.left)
            self.inorderTraversal(root.right)

    def postorderTraversal(self, root):
        if root is not None:
            self.inorderTraversal(root.left)
            self.inorderTraversal(root.right)
            print(root.value, end=' ')

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
    def treeSearch(self,value):
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
        while currentNode is not None and value is not currentNode.value:
            if value < currentNode.value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return currentNode

    def treeMinimum(self, subRoot):
        currentNode = subRoot
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode

    def treeMaximum(self, subRoot):
        currentNode = subRoot
        while currentNode.right is not None:
            currentNode = currentNode.right
        return currentNode

    def nodeSuccessor(self, subRoot):
        currentNode = subRoot
        if currentNode.right is not None:
            return self.treeMinimum(currentNode.right)
        prev = currentNode.parent
        while prev is not None and currentNode is prev.right:
            currentNode = prev
            prev = prev.parent
        return prev

    def nodePredecessor(self, subRoot):
        currentNode = subRoot
        if currentNode.left is not None:
            return self.treeMaximum(currentNode.left)
        prev = currentNode.parent
        while prev is not None and currentNode is prev.left:
            currentNode = prev
            prev = prev.parent
        return prev

    def transplant(self, oldRoot, newRoot):
        if oldRoot.parent is None:
            self.root = newRoot
        elif oldRoot is oldRoot.parent.left:
            oldRoot.parent.left = newRoot
        else:
            oldRoot.parent.right = newRoot
        if newRoot is not None:
            newRoot.parent = oldRoot.parent

    def deleteNode(self, node):
        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node,node.left)
        else:
            y = self.treeMinimum(node.right)
            if y.parent is not node:
                self.transplant(y,y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node,y)
            y.left = node.left
            y.left.parent = y

    # Finds k-th smallest value
    def osSelectSmallest(self,root,k):
        currentNode = self.treeMinimum(root)
        for i in range(k-1):
            currentNode = self.nodeSuccessor(currentNode)
        if currentNode is None:
            return None
        return currentNode.value

    # Finds k-th biggest value
    def osSelectBiggest(self,root,k):
        currentNode = self.treeMaximum(root)
        for i in range(k-1):
            currentNode = self.nodePredecessor(currentNode)
        if currentNode is None:
            return None
        return currentNode.value

    # TODO rimuovere se non si usa
    def size(self,root):
        if root is None:
            return 0
        return self.size(root.left) + self.size(root.right) + 1



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
            return rankLeft + rankRight"""

    # FIXME per i valori non presente restituisce il rango più alto, invece di None
    def osRank(self,node,target):
        if node is None:
            return 0
        successor = self.nodeSuccessor(self.treeMinimum(self.root))
        rank = 1
        while successor is not None and successor.value <= target:
            rank += 1
            successor = self.nodeSuccessor(successor)
        return rank

albero = BST()

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
print("60 è nel bst?",albero.treeSearch(60))
print("il max è: ", albero.treeMaximum(albero.root).value)
print("il min è: ", albero.treeMinimum(albero.root).value)

print("\nil predecessore di 40: ", albero.nodePredecessor(albero.searchNode(40)).value)

print("il 7 valore più piccolo è ", albero.osSelectSmallest(albero.root,7))


print("il rango di 20 è: ", albero.osRank(albero.root,20))
#print("nodo 40 :",albero.searchNode(40).value)
#albero.treeDelete(albero.searchNode(40))
#albero.inorderTraversal(albero.root)


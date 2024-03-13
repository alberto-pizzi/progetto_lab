class BSTNode:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
        self.parent = None

    # TODO rimuovere se necessario
    def getValue(self):
        return self.value
    def setValue(self,value):
        self.value = value
    def getLeftChild(self):
        return self.left
    def setLeftChild(self,value):
        self.left = value
    def getRightChild(self):
        return self.right
    def setRightChild(self, value):
        self.right = value

class BST:
    def __init__(self):
        self.root = None
    # TODO rimuovere se necessario
    def getRoot(self):
        return self.root

    def inorderTraversal(self,root):
        if root is not None:
            self.inorderTraversal(root.left)
            print(root.getValue(), end=' ')
            self.inorderTraversal(root.right)

    def preorderTraversal(self, root):
        if root is not None:
            print(root.getValue(), end=' ')
            self.inorderTraversal(root.left)
            self.inorderTraversal(root.right)
    def postorderTraversal(self, root):
        if root is not None:
            self.inorderTraversal(root.left)
            self.inorderTraversal(root.right)
            print(root.getValue(), end=' ')

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
        if (value < prev.value):
            prev.left = newNode
        else:
            prev.right = newNode

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


    #FIXME
    def treeMinimum(self, subRoot):
        currentNode = subRoot
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value
    #FIXME
    def treeMaximum(self, subRoot):
        currentNode = subRoot
        while currentNode.right is not None:
            currentNode = currentNode.right
        return currentNode.value
    #FIXME
    def treeSuccessor(self, subRoot):
        currentNode = subRoot
        if currentNode.right is not None:
            return self.treeMinimum(currentNode.right)
        prev = currentNode.parent
        while prev is not None and currentNode is prev.right:
            current = prev
            prev = prev.parent
        return prev

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
print("il max è: ", albero.treeMaximum())
print("il min è: ", albero.treeMinimum())

#print("\nil successore di 30: ", albero.treeSuccessor(30))


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

    def treeSuccessor(self, subRoot):
        currentNode = subRoot
        if currentNode.right is not None:
            return self.treeMinimum(currentNode.right)
        prev = currentNode.parent
        while prev is not None and currentNode is prev.right:
            currentNode = prev
            prev = prev.parent
        return prev
    def treePredecessor(self, subRoot):
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

    def treeDelete(self,node):
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

print("\nil predecessore di 40: ", albero.treePredecessor(albero.searchNode(40)).value)
#print("nodo 40 :",albero.searchNode(40).value)
#albero.treeDelete(albero.searchNode(40))
#albero.inorderTraversal(albero.root)


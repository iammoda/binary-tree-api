class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class binaryTree(object):
    def __init__(self):
        self.root = None

    def printTraversal(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorderTraversal(self.root)
        elif traversal_type == "inorder":
            return self.inorderTraversal(self.root)
        elif traversal_type == "postorder":
            return self.postorderTraversal(self.root)
        else:
            print("traversal type " + str(traversal_type) + "is not supported.")

    def preorderTraversal(self, root, traversal=""):
        if root:
            traversal += (str(root.value) + "-")
            traversal = self.preorderTraversal(root.left, traversal)
            traversal = self.preorderTraversal(root.right, traversal)
        return traversal

    def inorderTraversal(self, root, traversal=""):
        if root:
            traversal = self.inorderTraversal(root.left, traversal)
            traversal += (str(root.value) + "-")
            traversal = self.inorderTraversal(root.right, traversal)
        return traversal

    def postorderTraversal(self, root, traversal=""):
        if root:
            traversal = self.inorderTraversal(root.left, traversal)
            traversal = self.inorderTraversal(root.right, traversal)
            traversal += (str(root.value) + "-")
        return traversal

    def search(self, nodeToFind):
        if self.root:
            isFound = self.searchHelper(nodeToFind, self.root)
            if isFound:
                return True
            return False
        else:
            return None

    def searchHelper(self, nodeToFind, root):
        if root.right and nodeToFind > root.value:
            return self.searchHelper(nodeToFind, root.right)
        elif root.left and nodeToFind < root.value:
            return self.searchHelper(nodeToFind, root.left)
        elif root.value == nodeToFind:
            return True

    def insert(self, nodeToInsert):
        if self.root is None:
            self.root = Node(nodeToInsert)
        else:
            self.insertHelper(nodeToInsert, self.root)

    def insertHelper(self, nodeToInsert, currentNode):
        if nodeToInsert < currentNode.value:
            if currentNode.left is None:
                currentNode.left = Node(nodeToInsert)
            else:
                self.insertHelper(nodeToInsert, currentNode.left)
        elif nodeToInsert > currentNode.value:
            if currentNode.right is None:
                currentNode.right = Node(nodeToInsert)
            else:
                self.insertHelper(nodeToInsert, currentNode.right)
        else:
            print("value is present in tree")


bst = binaryTree()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)


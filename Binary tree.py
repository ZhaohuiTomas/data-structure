class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeftChild(self,newkey):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newkey)
        else:
            t = BinaryTree(newkey)
            t.leftChild = self.leftChild
            self.leftChild = t
    def insertRightChild(self,newkey):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newkey)
        else:
            t = BinaryTree(newkey)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootValue(self,Obj):
        self.key = Obj

    def getRootValue(self):
        return self.key
if __name__ == "__main__":
r = BinaryTree('a')
print(r.getRootValue())
print(r.getLeftChild())
r.insertLeftChild('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootValue())
r.insertRightChild('c')
print(r.getRightChild())
print(r.getRightChild().getRootValue())
r.getRightChild().setRootValue('hello')
print(r.getRightChild().getRootValue())
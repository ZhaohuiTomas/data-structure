"""
本节内容是利用分析树解决（3+（4*5））问题。
"""
#需要用到栈的性质，因此下面输出一个之前定义好的栈
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
#也要用到Binary Tree的性质
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




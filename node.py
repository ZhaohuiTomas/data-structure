class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

if __name__ == "__main__":
    test = Node(96)
    test.setData(68)
    test.setNext(54)
    print(test.getData(),test.next)
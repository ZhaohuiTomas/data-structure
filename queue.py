class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):
        return self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
if __name__ == "__main__":
    s = Queue()
    s.enqueue(2)
    s.enqueue("2")
    print(s.size())
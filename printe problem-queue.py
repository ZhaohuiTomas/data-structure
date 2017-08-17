from queue import Queue

#定义打印机类的属性
class Printer:
    def __init__(self,ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining  = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages()*60/self.pagerate

import random
#定义一个任务类
class Task:
    def __init__(self,time):
        self.timeStamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timeStamp

    def getPages(self):
        return self.pages

    def waiteTime(self,currentTime):
        return currentTime - self.timeStamp

#求解问题函数
def simulation(numSeconds,pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for  currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waiteTime(currentSecond))
            labprinter.startNext(nexttask)
        labprinter.tick()
    averagetime = sum(waitingtimes) / len(waitingtimes)
    print("Average time is %6.2f secs %d tasks remaining"%(averagetime,printQueue.size()))

def newPrintTask():
    if random.randrange(1,181) == 180:
        return True
    else:
        return False

if __name__ == "__main__":
    for i in range(10):
        simulation(3600,10)
    print("-*-"*15)
    for i in range(10):
        simulation(3600,5)
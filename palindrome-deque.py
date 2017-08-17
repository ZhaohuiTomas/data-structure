from deque import Deque

def palindromCheck(String):
    stringDeque = Deque()
    for string in String:
        stringDeque.addFront(string)
    stillTrue = True
    while stringDeque.size() > 1 and stillTrue:
        first = stringDeque.removeRear()
        last = stringDeque.removeFront()
        if first != last:
            stillTrue = False


    return stillTrue

if __name__ == "__main__":
    print(palindromCheck("roor"))

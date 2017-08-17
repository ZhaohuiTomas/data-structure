# def sequenceSearch(item, searchList)
#     length = len(searchList)
#     found = False
#     for i in range(length):
#         if searchList[i] == item:
#             found = True
#     return found
"""
直接按照顺序查找法
"""
def sequenceSearch(item, searchList):
    pos = 0
    found = False
    while pos < len(searchList) and not found:
        if searchList[pos] == item:
            found = True
        else:
            pos += 1
    return found


"""
有序算法的排序方法
"""

def sequenceOrder(item, searchList):
    pos = 0
    foud = False
    while pos < len(searchList) and not foud:
        if searchList[pos] == item:
            foud = True
        elif searchList[pos] > item:
            break
        else:
            pos += 1
    return foud,pos
print(sequenceOrder(25,[1,2,3,4,5,6734,325235]))



"""
有序的二分查找算法
"""

def binarySearch(item, seachList):
    first = 0
    last = len(seachList) - 1
    found = False
    while not found and first <= last:
        mid = (first + last) // 2
        if item == seachList[mid]:
            found = True
        else:
            if item < seachList[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

print(binarySearch(13, [0, 1, 2, 8, 13, 17, 19, 32, 42,]))


"""
有序二分查找的递归形式
"""

def cursionBinary(item, searchList):
    if len(searchList) == 0:
        return False
    else:
        midpoint = len(searchList) // 2
        if searchList[midpoint] == item:
            return True
        else:
            if searchList[midpoint] > item:
                return cursionBinary(item, searchList[:midpoint])
            else:
                return cursionBinary(item, searchList[midpoint+1:])

print(cursionBinary(3, [0, 1, 2, 8, 13, 17, 19, 32, 42,]))

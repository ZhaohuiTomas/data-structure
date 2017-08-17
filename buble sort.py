def bubleSort(alist):              #冒泡排序
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist
alist=[23,23,34,56,34,59]
print(bubleSort(alist))

#alist = [3,4,5,2,34,53,42,34]
def shortbubleSort(alist):       #短冒泡排序，会在中间判断是否已经是拍好的序列
    passnum = len(alist) - 1
    exchange = True
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchange = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum -= 1


print(shortbubleSort(alist))
print(alist)


def selectionsort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positonofMAx = 0
        for location in range(1,1+fillslot):
            if alist[location] > alist[positonofMAx]:
                positonofMAx = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positonofMAx]
        alist[positonofMAx] = temp

alist = [232,343,23,243,5,232,3432,4]
print(selectionsort(alist))
print(alist)

def insertsort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position -1
        alist[position] = currentvalue

alist = [23,24,212,4,322,23422,342,34]
print(insertsort(alist))
print(alist)



def  shellsort(alist):
    length = len(alist)
    listgap = length // 2
    while  listgap > 0:
        begin = 0
        while begin + listgap <= length -1:
            if alist[begin] > alist[begin+listgap]:
                temp = alist[begin]
                alist[begin] = alist[begin+listgap]
                alist[begin+listgap] = temp
            begin += 1
        listgap //= 2

alist = [23,23,4,354,4,45,4334,12,124]
print(shellsort(alist))
print(alist)

l= 0
g = 0
p = 0
m = 0
def mergeSort(alist):
    global l,g,p,m
    l += 1
    print("Begin spliting %d time"%l,alist)

    if len(alist) > 1:
        mid = len(alist) // 2
        leflist = alist[:mid]
        rightlist = alist[mid:]
        g += 1
        print("l_part split %d time"%g,leflist)
        mergeSort(leflist)
        p += 1
        mergeSort(rightlist)
        print("second split %d time" % p,rightlist)

        i,j,k = 0,0,0
        while i < len(leflist) and j < len(rightlist):
            if leflist[i] < rightlist[j]:
                alist[k] = leflist[i]
                i += 1
            else:
                alist[k] = rightlist[j]
                j += 1
            k += 1
        while i < len(leflist):
            alist[k] = leflist[i]
            i += 1
            k += 1
        while j < len(rightlist):
            alist[k] = rightlist[j]
            j += 1
            k += 1
    m += 1
    print("merging %d time"%m,alist)



alist = [2,3,24,43,5,34,52,3,223,454,3,42]
print(mergeSort(alist))

"""
下面实现，快速排序
"""


# def qsort_rec(alist,l,r):
#     if l > r:
#         return
#     medium = alist[l]
#     l_part = l+1
#     r_part = r
#     while l_part < r_part:
#         if medium > alist[l_part]:
#             alist[l_part] = alist[l_part+1]
#             alist[l_part+1] = medium
#             l_part +=1
#         if medium < alist[r_part]:
#             r_part -= 1
#         #if medium <= alist[l_part+1] and medium >= alist[r_part]:
#         else:
#             pivot = alist[r_part]
#             alist[r_part] = alist[l_part]
#             alist[l_part] = pivot
#             l_part += 1
#             r_part -= 1
#     alist[l_part] = medium
#     qsort_rec(alist,l,l_part-1)
#     qsort_rec(alist,l_part+1,r)
#
# def quick_sort(alist):
#     qsort_rec(alist,0,len(alist)-1)
#
# alist =[1,34,45,6,34,3,5,6,757,897,85767,645]
# print(quick_sort(alist))
# print(alist)

def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and pivotvalue >= alist[leftmark]:
            leftmark += 1
        while leftmark <= rightmark and pivotvalue <= alist[rightmark]:
            rightmark -= 1
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark

def quicksortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)

        quicksortHelper(alist,first,splitpoint-1)
        quicksortHelper(alist,splitpoint+1,last)

def quicksort(alist):
    quicksortHelper(alist,0,len(alist)-1)

alist = [54,26,23,2352,23,23,23,2454,543,93,17,77,31,44,55,20]
quicksort(alist)
print(alist)


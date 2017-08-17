
"""
这个算法复杂度太大，不宜采用

def recMc(coinValueList,change):
    mincoin = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numcoins = 1 + recMc(coinValueList,change-i)
            if numcoins < mincoin:
                mincoin = numcoins
        return mincoin


print(recMc([1,5,10,25],63))

"""

def recMe(coinValueList,change,knowlist):
    mincoin = change
    if change in coinValueList:
        knowlist[change] = 1
        return 1
    elif knowlist[change] > 0:
        return knowlist[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            nums = 1 + recMe(coinValueList,change - i,knowlist)
            if nums < mincoin:
                mincoin = nums
                knowlist[change] = mincoin
    return mincoin

print(recMe([1,2,5,10],63,[0]*64))


"""
map 抽象数据类型定义如下。该结构是键与值之间的关联的无序集合。map中的键都是唯一的，
因此键和值之间存在一对一的关系。操作如下。
Map() 创建一个新的 map 。它返回一个空的 map 集合。
put(key，val) 向 map 中添加一个新的键值对。如果键已经在 map 中，那么用新值替换旧值。
get(key) 给定一个键，返回存储在 map 中的值或 None。
del 使用 del map[key] 形式的语句从 map 中删除键值对。
len() 返回存储在 map 中的键值对的数量。
in 返回 True 对于 key in map 语句，如果给定的键在 map 中，否则为False。

"""

class Hashtable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self,key,size):
        return key % size

    def rehashfunction(self,oldhash,size):
        return (oldhash + 1) % seize
    def putvalue(self,key,data):
        hashvalue = self.hashfunction(key,len(self.slots))
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehashfunction(hashvalue,len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehashfunction(nextslot,len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data
    def getvalue(self,key):
        startslot = self.hashfunction(key,len(self.slots))
        found = False
        stop = False
        position = startslot
        while self.slots[startslot] != None and not found and not stop:
            if self.slots[position] == key:
                data = self.data[position]
                found = True
            else:
                position = self.rehashfunction(position,len(self.slots))
                if position == startslot:
                    stop = True
        return  data
    def __getitem__(self, key):
        return self.getvalue(key)
    def __setitem__(self, key, data):
        self.putvalue(key,data)


H = Hashtable()
H[54]="cat"
H[75]="dog"
H[63]="mice"
H[58]="goat"
H[55]="pig"
print(H.slots)



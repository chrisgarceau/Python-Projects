# Christopher Garceau
# 1/10/2023

# Least Recently Used (LRU) is a cache replacement algorithm that replaces cache when the space is full. 
# It allows us to access the values faster by removing the least recently used values. 
#
# Three methods of a LRU cache:
#   - put(key, value) should store key and associate it with value. If key does not alreadv exist in the cache, add it. If it does, update the value.
#   - get(key) should retrieve the value associated with key. If the key does not exist, return -1
#   - last() should return the key most recentlv accessed by either a get or put call.
#
# The object should also take a maximum capacity.
# Once capacity is reached, additional calls to put should result in the least recently accessed key and 
# its associated value being discarded in favor of the new key/value pair.

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity) -> None:
        self.capacity = capacity    # max. capacity of the LRU cache
        self.dict = OrderedDict()   # stores key/value pairs
        self.recentAccessList = ""  # stores most recently accessed by either get or put call


    def put(self, key, val):
        if len(self.dict) < self.capacity:
            if key in self.dict:
                self.dict[key] = val
            else:
                newItem = { key : val }
                self.dict.update(newItem)

            self.recentAccessList = key

        elif len(self.dict) == self.capacity:
            if key in self.dict:
                self.dict[key] = val
            else:
                self.dict.popitem(last=False)
                newItem = { key : val }
                self.dict.update(newItem)
            
            self.recentAccessList = key
           

    def get(self, key):
        if key in self.dict:
            self.recentAccessList = key
            print(self.dict.get(key))
        else:
            print(-1)


    def last(self):
        print(self.recentAccessList)



# Testing
capacity = 2
obj = LRUCache(capacity)

obj.put("a", 1)
obj.get("a")
obj.last()
obj.put("b", 2)
obj.last()
obj.put("c", 3)
obj.get("a")
obj.get("b")
obj.get("c")
obj.put("b", 4)
obj.get("b")
obj.put("b", 5)
obj.put("b", 10)
obj.put("c", 8)
obj.last()
obj.put("d", 7)
obj.put("c", 10)
obj.put("z", 5)
obj.last()
obj.get("b")
obj.last()
obj.get("d")
obj.last()

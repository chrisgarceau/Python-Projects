# Christopher Garceau
# 1/10/2023

# Least Recently Used (LRU) is a cache replacement algorithm that replaces cache when the space is full. 
# It allows us to access the values faster by removing the least recently used values. 
#
# Three methods of a LRU cache:
#   - put(key, value) should store key and associate it with value. If key does not alreadv exist in the cache, add it. If it does, update the value.
#   - get(key) should retrieve the value associated with key. If the key does not exist, return -1
#   - last() should return the key most recently accessed by either a get or put call.
#
# The object should also take a maximum capacity.
# Once capacity is reached, additional calls to put should result in the least recently accessed key and 
# its associated value being discarded in favor of the new key/value pair.

class LRUCache:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.dict = {}
        self.recentAccessList = []

    def put(self, key, val):
        if len(self.dict) < self.capacity:
            if key in self.dict:
                self.dict[key] = val
            elif key not in self.dict:
                newItem = { key : val}
                self.dict.update(newItem)

            self.recentAccessList.append(key)

        elif len(self.dict) == self.capacity:
            if key in self.dict:
                self.dict[key] = val
            else:
                self.dict.pop(self.recentAccessList[0])
                newItem = { key : val}
                self.dict.update(newItem)
           
    def get(self, key):
        if key in self.dict:
            self.recentAccessList.append(key)
            print(self.dict.get(key))
        else:
            print(-1)

    def last(self):
        print(self.recentAccessList[-1])



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

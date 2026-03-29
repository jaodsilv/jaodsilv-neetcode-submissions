class MyHashMap:
    def __init__(self):
        self.hkeys = []
        self.keys = [-1] * 20000
        self.values = [-1] * 20000
        self.size = 0

    def put(self, key: int, value: int) -> None:
        # If size is big enough or happens to have a conflict, we change the size
        hkey = key.__hash__() % len(self.values)

        if self.keys[hkey] != key: # Key already in use
            while self.values[hkey] >= 0: # While there is collision
                self.__expand()
                hkey = key.__hash__() % len(self.values)

            # No collision
            self.size += 1
            self.keys[hkey] = key
            self.hkeys.append(hkey)
        self.values[hkey] = value

    def get(self, key: int) -> int:
        hkey = key.__hash__() % len(self.values)
        if self.keys[hkey] == key:
            return self.values[hkey]
        return -1

    def remove(self, key: int) -> None:
        hkey = key.__hash__() % len(self.values)
        if self.keys[hkey] != key:
            return # Nothing to do

        self.values[hkey] = -1
        self.keys[hkey] = -1
        self.size -= 1

    def __getItems(self):
        for h in self.hkeys:
            if self.values[h] >= 0:
                yield (self.keys[h], self.values[h])

    def __expand(self):
        oldSize = len(self.values)
        growth = (11 * oldSize) // 10
        newSize = oldSize + growth
        pairs = self.__getItems()
        while not self.__tryExpand(newSize, pairs):
            newSize += growth

    def __tryExpand(self, newSize, pairs) -> bool:
        hkeys = []
        values = [-1] * newSize
        keys = [-1] * newSize
        for k, v in pairs:
            hkey = k.__hash__() % newSize
            if keys[hkey] >= 0:
                return False
            hkeys.append(hkey)
            keys[hkey] = k
            values[hkey] = v

        self.hkeys = hkeys
        self.values = values
        self.keys = keys
        return True

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
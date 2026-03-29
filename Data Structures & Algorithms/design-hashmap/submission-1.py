class MyHashMap:
    def __init__(self):
        self.keys = []
        self.items = [None] * 100
        self.size = 0

    def put(self, key: int, value: int) -> None:
        # If size is big enough or happens to have a conflict, we change the size
        hkey = key.__hash__() % len(self.items)

        if not self.items[hkey]:
            self.items[hkey] = [(key, value)]
            self.size += 1
            self.keys.append(key)
        else:
            i = 0
            items = self.items[hkey]
            while i < len(items):
                if items[i][0] == key:
                    self.items[hkey][i] = (key, value)
                    break
                i += 1

            if i == len(items):
                self.items[hkey].append((key, value))
                self.keys.append(key)
                self.size += 1

        if len(self.items) < 2 * self.size:
            self.__expand()

    def get(self, key: int) -> int:
        hkey = key.__hash__() % len(self.items)
        if not self.items[hkey]:
            return -1

        for k, v in self.items[hkey]:
            if k == key:
                return v

        return -1

    def remove(self, key: int) -> None:
        hkey = key.__hash__() % len(self.items)
        if not self.items[hkey]:
            return # Nothing to do

        for k, v in self.items[hkey]:
            if k == key:
                self.items[hkey].remove((k, v))
                self.size -= 1
                return

    def __getItems(self) -> list:
        res = []
        size = len(self.items)
        for k in self.keys:
            if self.items[k.__hash__() % size] is not None:
                res.append((k, self.items[k.__hash__() % size]))
        return res

    def __expand(self):
        oldSize = len(self.items)
        newSize = (5 * oldSize) // 2
        pairs = self.__getItems()
        self.items = [None]*newSize
        for k, v in pairs:
            self.put(k, v)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
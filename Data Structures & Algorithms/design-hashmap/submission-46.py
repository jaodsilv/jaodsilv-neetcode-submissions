class MyHashMap:
    TABLESIZE = 101
    def __init__(self):
        self.table = [[] for _ in range(self.TABLESIZE)]

    def put(self, key: int, value: int) -> None:
        l = self.table[self.__hash(key)]
        if (len(l) > 0 and l[0][0] != key) or (len(l) > 1 and l[1][0] != key):
            print(f'collision: {l}; key: {key}')
            return

        for pair in l:
            if pair[0] == key:
                pair[1] = value
                return
        l.append([key, value])

    def get(self, key: int) -> int:
        l = self.table[self.__hash(key)]
        for k, v in l:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        l = self.table[self.__hash(key)]
        i = 0
        while i < len(l) and l[i][0] != key:
            i += 1
        if i < len(l):
            l[i] = l[-1]
            l.pop()
        
    @classmethod
    def __hash(cls, key: int) -> int:
        return key.__hash__() % cls.TABLESIZE

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
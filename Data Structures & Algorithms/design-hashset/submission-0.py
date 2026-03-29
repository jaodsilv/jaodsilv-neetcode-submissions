class MyHashSet:

    def __init__(self):
        self.__data = [-1]*10000

    def add(self, key: int) -> None:
        self.__data[self.__hash(key)] = key

    def remove(self, key: int) -> None:
        hkey = self.__hash(key)
        if self.__data[hkey] == key:
            self.__data[hkey] = -1
        

    def contains(self, key: int) -> bool:
        return self.__data[self.__hash(key)] == key

    def __hash(self, key: int) -> int:
        return key.__hash__() % len(self.__data)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
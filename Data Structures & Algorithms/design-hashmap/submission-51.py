class LL:
    def __init__(self, key, value):
        self.arr = [key, value, []]

    def add(self, key, value):
        node = self.arr

        if len(node) > 0:
            if node[0] == key:
                node[1] = value
            else:
                while node[2] and node[2][0] != key:
                    node = node[2]
                if node[2]:
                    node[2][1] = value
                else:
                    node[2] = [key, value, []]
        else:
            self.arr = [key, value, []]

    def remove(self, key) -> bool:
        node = self.arr

        if len(node) > 0:
            if node[0] == key:
                self.arr = node[2]
                return True
            else:
                while node[2] and node[2][0] != key:
                    node = node[2]
                if node[2]:
                    node[2] = node[2][2]
                    return True
        return False

    def get(self, key):
        node = self.arr

        if len(node) > 0:
            if node[0] == key:
                return node[1]
            else:
                while node[2] and node[2][0] != key:
                    node = node[2]
                if node[2]:
                    return node[2][1]
        return -1

class MyHashMap:
    BASE_LENGTH = 10000
    THRESHOLD = 0.7

    def __init__(self):
        self.arr = [None]*self.BASE_LENGTH

    def put(self, key: int, value: int) -> None:
        hkey = self._hkey(key)
        if self.arr[hkey]:
            self.arr[hkey].add(key, value)
        else:
            self.arr[hkey] = LL(key, value)

    def get(self, key: int) -> int:
        hkey = self._hkey(key)
        if self.arr[hkey]:
            return self.arr[hkey].get(key)
        return -1

    def remove(self, key: int) -> None:
        hkey = self._hkey(key)
        if self.arr[hkey]:
            self.arr[hkey].remove(key)

    def _hkey(self, key: int) -> int:
        return key.__hash__() % self.BASE_LENGTH


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
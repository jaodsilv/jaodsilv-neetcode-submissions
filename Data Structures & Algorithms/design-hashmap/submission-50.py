class Node:
    def __init__(self, key, value, prev = None) -> None:
        self.key = key
        self.value = value
        self.next = None
        if prev:
            prev.next = self
        self.prev = prev

    def remove(self, key):
        if key == self.key:
            if self.prev:
                self.prev.next = self.next
                return self.prev
            else:
                return self.next
        elif self.next:
            self.next.remove(key)
            if self.prev:
                return self.prev
            else:
                return self
        else:
            return self

    def update(self, key, value):
        if self.key == key:
            self.value = value
        elif self.next:
            self.next.update(key, value)
        else:
            Node(key, value, self)

    def get(self, key):
        if self.key == key:
            return self.value
        elif self.next:
            self.next.get(key)
        else:
            return -1

class MyHashMap:
    SIZE = 15000
    def __init__(self):
        self.map = [None]*self.SIZE

    def put(self, key: int, value: int) -> None:
        hkey = self._hash(key)
        if self.map[hkey]:
            self.map[hkey].update(key, value)
        else:
            self.map[hkey] = Node(key, value)

    def get(self, key: int) -> int:
        hkey = self._hash(key)
        if self.map[hkey]:
            return self.map[hkey].get(key)
        else:
            return -1

    def remove(self, key: int) -> None:
        hkey = self._hash(key)
        if self.map[hkey]:
            self.map[hkey] = self.map[hkey].remove(key)


    def _hash(self, key) -> int:
        return hash(key) % self.SIZE

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
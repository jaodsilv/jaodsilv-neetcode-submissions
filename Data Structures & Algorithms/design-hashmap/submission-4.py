class LLNode:
    def __init__(self, key: int = -1, value: int = -1, next = None) -> None:
        self.key = key
        self.value = value
        self.next = next

    def remove(self, key: int):
        if self.key == key:
            return self.next

        node = self
        while node.next and node.next.key != -1 and node.next.key != key:
            node = node.next
        if node.next and node.next.key == key:
            node.next = node.next.next
        return self
    
    def get(self, key: int) -> int:
        node = self
        while node.key != -1 and node.key != key:
            node = node.next
        return node.value

class MyHashMap:
    def __init__(self):
        self.buckets = [LLNode() for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        # If size is big enough or happens to have a conflict, we change the size
        self.remove(key)
        hkey = self.__hashKey(key)
        self.buckets[hkey] = LLNode(key, value, self.buckets[hkey])

    def get(self, key: int) -> int:
        return self.buckets[self.__hashKey(key)].get(key)

    def remove(self, key: int) -> None:
        hkey = self.__hashKey(key)
        self.buckets[hkey] = self.buckets[hkey].remove(key)

    def __hashKey(self, key: int, size: int = 1000) -> int:
        return key.__hash__() % size

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
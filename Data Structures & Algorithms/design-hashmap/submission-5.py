class LLNode:
    def __init__(self, key: int = -1, value: int = -1) -> None:
        self.key = key
        self.value = value
        self.next = None

    def put(self, key: int, value: int) -> None:
        node = self
        while node.next and node.next.key != key:
            node = node.next
        if node.next:
            node.next.value = value
        else:
            node.next = LLNode(key, value)

    def remove(self, key: int):
        node = self
        while node.next and node.next.key != key:
            node = node.next
        if node.next:
            node.next = node.next.next
    
    def get(self, key: int) -> int:
        node = self.next
        while node and node.key != key:
            node = node.next
        return node.value if node else -1

class MyHashMap:
    def __init__(self):
        self.buckets = [LLNode() for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        # If size is big enough or happens to have a conflict, we change the size
        self.buckets[self.__hashKey(key)].put(key, value)

    def get(self, key: int) -> int:
        return self.buckets[self.__hashKey(key)].get(key)

    def remove(self, key: int) -> None:
        self.buckets[self.__hashKey(key)].remove(key)

    def __hashKey(self, key: int, size: int = 1000) -> int:
        return key.__hash__() % size

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
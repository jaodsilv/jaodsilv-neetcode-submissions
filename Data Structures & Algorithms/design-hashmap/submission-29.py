class LLNode:
    def __init__(self, key: int = -1, value: int = -1) -> None:
        self.key = key
        self.value = value
        self.next = None

    def put(self, key: int, value: int) -> bool:
        node = self
        while node.next and node.next.key != key:
            node = node.next

        if node.next:
            node.next.value = value
            return False

        node.next = LLNode(key, value)
        return True

    def remove(self, key: int):
        node = self
        while node.next and node.next.key != key:
            node = node.next
        if node.next:
            node.next = node.next.next
            return True
        return False
    
    def get(self, key: int) -> int:
        node = self.next
        while node and node.key != key:
            node = node.next
        return node.value if node else -1

class MyHashMap:
    def __init__(self):
        self.buckets = [LLNode() for _ in range(64)]
        self.cap = 64
        self.size = 0
        self.collisions = 0

    def put(self, key: int, value: int) -> None:
        # If size is big enough or happens to have a conflict, we change the size
        hkey = self.__hashKey(key)
        if self.buckets[hkey].put(key, value):
            self.size += 1
        if self.buckets[hkey].next and self.buckets[hkey].next.next:
            self.collisions += 1
            print(self.collisions)
        if self.size / self.cap > 0.75:
            self.__expand()
        if self.collisions > 1:
            raise Exception

    def get(self, key: int) -> int:
        return self.buckets[self.__hashKey(key)].get(key)

    def remove(self, key: int) -> None:
        if self.buckets[self.__hashKey(key)].remove(key):
            self.size -= 1

    def __hashKey(self, key: int, cap: int = 0) -> int:
        if cap:
            return key.__hash__() % cap
        return key.__hash__() % self.cap

    def __expand(self):
        print("expanded", self.collisions)
        for _ in range(self.cap):
            self.buckets.append(LLNode())

        self.cap *= 2

        for i, node in enumerate(self.buckets):
            while node.next:
                key = node.next.key
                hkey = self.__hashKey(key)
                if hkey != i:
                    self.buckets[hkey].put(key, node.next.value)
                    node.next = node.next.next
                else:
                    node = node.next
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
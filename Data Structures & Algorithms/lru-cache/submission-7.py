from collections import OrderedDict
# LinkedList solution
class LLNode:
    def __init__(self, key, value, left=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = None

    def selfRemove(self):
        if self.left:
            self.left.right = self.right
        if self.right:
            self.right.left = self.left
        return self.right

    def move_to_end(self, head, tail):
        if head.key == self.key and self.right:
            head = self.right
        if tail.key != self.key:
            self.selfRemove()
            tail.right = self
            self.left = tail
            self.right = None
        return head

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = None
        self.tail = None
        self.pointers = {}

    def get(self, key: int) -> int:
        if key not in self.pointers:
            print(404, self.head.key if self.head else None, self.tail.key if self.tail else None)
            return -1
        node = self.pointers[key]
        if self.cap > 1:
            self.head = node.move_to_end(self.head, self.tail)
            self.tail = node
        print("get", key, node.val, None if self.head is None else self.head.key, None if self.tail is None else self.tail.key)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.pointers:
            node = LLNode(key, value, self.tail)
            if self.head is None:
                self.head = node
                self.tail = node
            else:
                self.tail.right = node
                self.tail = node
            self.pointers[key] = node
            if len(self.pointers) > self.cap:
                del self.pointers[self.head.key]
                self.head = self.head.selfRemove()
            print("New", key, value, self.head.key if self.head else None, self.tail.key if self.tail else None)
        else:
            node = self.pointers[key]
            self.head = node.move_to_end(self.head, self.tail)
            self.tail = node
            node.val = value
            print("Update", key, value, self.head.key if self.head else None, self.tail.key if self.tail else None)

# Ordered Dict solution
# class LRUCache:
    # def __init__(self, capacity: int):
    #     self.cache = OrderedDict()
    #     self.cap = capacity

    # def get(self, key: int) -> int:
    #     if key not in self.cache:
    #         return -1
    #     self.cache.move_to_end(key)
    #     return self.cache[key]

    # def put(self, key: int, value: int) -> None:
    #     if key in self.cache:
    #         self.cache.move_to_end(key)
    #     self.cache[key] = value
    #     if len(self.cache) > self.cap:
    #         self.cache.popitem(last=False) # Removes first
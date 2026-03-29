# My own solution
from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.slots = capacity
        self.queue = deque()
        self.kvs = {} # maps key to pairs (lastUse, value)
        self.time = 0


    def get(self, key: int) -> int:
        if key not in self.kvs:
            return -1
        pair = self.kvs[key]
        self.kvs[key] = (self.time, pair[1])
        self.queue.append((self.time, key))
        while len(self.queue) > 1 and self.queue[0][1] == key:
            self.queue.popleft()
        self.time += 1
        return pair[1]

    def put(self, key: int, value: int) -> None:
        if key not in self.kvs:
            self.slots -= 1
        self.kvs[key] = (self.time, value)
        self.queue.append((self.time, key))
        if self.slots < 0:
            self.slots = 0
            popped = self.queue.popleft()
            lastUsed = self.kvs[popped[1]][0]
            while popped[0] != lastUsed:
                popped = self.queue.popleft()
                lastUsed = self.kvs[popped[1]][0]
            del self.kvs[popped[1]]
        self.time += 1

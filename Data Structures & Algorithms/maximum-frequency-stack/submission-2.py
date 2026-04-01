import heapq
class FreqStack:

    def __init__(self):
       self.heap = []
       self.values = defaultdict(int)
       self.__len = 0

    # O(log(n))
    def push(self, val: int) -> None:
        self.values[val] += 1
        heapq.heappush_max(self.heap, [self.values[val], self.__len, val])
        self.__len += 1
        # print(self.heap)

    # O(nlog(n)) worst case. O(logn) average case
    def pop(self) -> int:
        val = heapq.heappop_max(self.heap)[2]
        self.values[val] -= 1
        return val



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
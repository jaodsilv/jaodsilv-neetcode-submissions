import heapq
class FreqStack:

    def __init__(self):
       self.heap = []
       self.values = {}
       self.__len = 0

    def push(self, val: int) -> None:
        if val in self.values:
            self.values[val][2].append(self.__len)
            if self.heap and self.heap[0][1] == val:
                self.values[val][0] += 1
                heapq.heapreplace_max(self.heap, self.values[val])
            else:
                self.values[val][1] = -1
                self.values[val] = [self.values[val][0] + 1, val, self.values[val][2]]
                heapq.heappush_max(self.heap, self.values[val])
        else:
            self.values[val] = [1, val, [self.__len]]
            heapq.heappush_max(self.heap, self.values[val])
        self.__len += 1
        # print(self.heap)

    def pop(self) -> int:
        heap = self.heap
        while heap[0][1] == -1:
            heapq.heappop_max(heap)
        freq = heap[0][0]
        cand = []
        while heap and heap[0][0] == freq:
            element = heapq.heappop_max(heap)
            if element[1] >= 0:
                cand.append(element)
        chosen = cand[0]
        if len(cand) > 1:
            lastPos = 0
            for element in cand:
                if element[2][-1] > chosen[2][-1]:
                    chosen = element
            for element in cand:
                if element[1] != chosen[1]:
                    heapq.heappush_max(heap, element)
        if freq > 1:
            chosen[0] -= 1
            chosen[2].pop()
            heapq.heappush_max(heap, chosen)
        # print(chosen, heap)
        return chosen[1]



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
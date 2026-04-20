from collections import deque

class StockSpanner:

    def __init__(self):
        self.stack = []

    # Traveling over the list we O(n) for each next operation
    # To get a better result we could:
    # 1. compress to have only the maximums and number of days til there
    # 2. use a data structure which could allow us to find the number of days until the next value greater than or equals to n
    #    a. Maybe a segment tree could solve that.

    def next(self, price: int) -> int:
        count = 1
        while self.stack and self.stack[-1][0] <= price:
            count += self.stack.pop()[1]
        self.stack.append((price, count))
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
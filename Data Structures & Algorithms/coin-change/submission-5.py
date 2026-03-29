from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Looking at that, it looks like a bfs problem, finding the minimum path to the value
        # For simplicity we store the sum values, not the actual coins used
        if amount == 0:
            return 0
        queue = deque([0])
        coinsUsed = 0
        valuesTested = set()
        found = False
        while queue:
            coinsUsed += 1
            for _ in range(len(queue)):
                value = queue.popleft()
                for coin in coins:
                    newValue = value + coin
                    if newValue in valuesTested or newValue > amount:
                        continue
                    if newValue == amount:
                        return coinsUsed
                    valuesTested.add(newValue)
                    queue.append(newValue)
        return -1
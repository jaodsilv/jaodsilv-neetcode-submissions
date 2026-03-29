class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        if len(coins) == 1:
            if amount % coins[0] == 0:
                return amount // coins[0]
            else:
                return -1

        # First of all, let's sort reversed the coins:
        coins.sort()
        
        minPerVal = [None]*(amount + 1)
        minPerVal[0] = 0
        for i in range(1, len(minPerVal)):
            print(i-1, minPerVal[i-1])
            for j in range(len(coins)):
                if i - coins[j] < 0:
                    break
                if minPerVal[i - coins[j]] is not None:
                    if minPerVal[i] is None:
                        minPerVal[i] = minPerVal[i-coins[j]] + 1
                    else:
                        minPerVal[i] = min(minPerVal[i], minPerVal[i-coins[j]] + 1)
        return minPerVal[-1] if minPerVal[-1] is not None else -1

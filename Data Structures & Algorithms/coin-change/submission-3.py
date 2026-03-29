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
        coins.sort(reverse=True)
        
        # Now we go like a decision tree, where the next coin can be choosen among any of the next ones
        def pickCoin(curSum, i, total):
            #print(curSum, i, total)
            curSum += coins[i]
            total += 1

            if curSum == amount:
                return total

            if curSum > amount:
                return -1

            minCoins = -1
            for j in range(i, len(coins)):
                picked = pickCoin(curSum, j, total)

                if picked == -1:
                    continue
                if minCoins == -1:
                    minCoins = picked
                elif picked > -1:
                    if picked > minCoins:
                        return minCoins
                    minCoins = min(minCoins, picked)
            return minCoins

        minCoins = -1
        for i in range(len(coins)):
            val = pickCoin(0, i, 0)
            if minCoins == -1:
                minCoins = val
            elif val > -1:
                minCoins = min(val, minCoins)
        return minCoins

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        count = [0]*(max(stones) + 1)
        for w in stones:
            count[w] += 1
        maxStone = 0
        i = len(count) - 1
        while i > 0:
            print('i = ',  i)
            while count[i]:
                print(f'count[i] = count[{i}] = {count[i]}')
                print(f'maxStone = {maxStone}')
                count[i] -= 1
                if maxStone == 0:
                    maxStone = i
                else:
                    count[maxStone - i] += 1
                    i = max(i, maxStone - i)
                    maxStone = 0
            i -= 1
        return maxStone

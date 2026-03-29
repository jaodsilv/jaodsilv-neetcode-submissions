class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxValue = max(stones)
        values = [0]*(maxValue+1)
        print(maxValue)
        for stone in stones:
            values[stone] += 1
        i = maxValue
        curr = 0
        while i > 0:
            print(i)
            while i > 0 and values[i] == 0:
                i-=1
            if i == 0:
                break
            values[i] -= 1
            if curr == 0:
                curr = i
            else:
                values[curr-i] += 1
                i = max(i, curr-i)
                curr = 0
        return curr
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        Given the low range of possible numbers, let's bucket sort them
        '''
        buckets = [0]*(target+1)
        for num in candidates:
            if num <= target:
                buckets[num] += 1
        '''
        Now let's build the possibilities.
        Using DP to store a memory
        Target ->           0              1         2            3       4     5    6   7
            1  5  [[3,4],[2,5],[2,2,3]] [[2,4]] [[5],[2,3]] [[4],[2,2]] [[3]] [[2]] [] [[]]
            1  4
            1  3
            2  2
            1  1
            0  0
        '''
        while buckets and buckets[-1] == 0:
            buckets.pop()
        maxi = len(buckets)
        prefix = [0]

        # print(buckets)
        for j in range(1, len(buckets)):
            bucket = buckets[j]
            prefix.append(min(target, prefix[-1] + j*bucket))
        dp = [[] for _ in range(target)] + [[[]]]
        # if buckets[target]:
        #     res.append([target])
        for i in range(min(target, len(buckets)-1), 0, -1):
            # print(f'Augmenting DP[i], i={i}')
            for j in range(target-i+1):
                # print(f'j: {j}')
                amount = buckets[i]
                toAdd = []
                toMergeIndex = j
                for _ in range(amount):
                    toAdd.append(i)
                    toMergeIndex += i
                    if toMergeIndex > target:
                        break
                    for item in dp[toMergeIndex]:
                        dp[j].append(item + toAdd)
        # print(dp)
        return dp[0]



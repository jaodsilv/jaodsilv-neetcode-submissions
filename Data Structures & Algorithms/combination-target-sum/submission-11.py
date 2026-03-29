class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # All number are positives greater than 1
        # Let's think as a decision tree

        # Target is small
        # nums[i] is small
        # nums.length is small as well
        # Let's use arrays to store things
        
        res = []

        def choose(i, total, curr):
            #print(i, total, curr)
            if total > target:
                return
            if total == target:
                #print('added')
                res.append(curr.copy())
                #print(res)
                return
            for j in range(i, len(nums)):
                total += nums[j]
                curr.append(nums[j])
                choose(j, total, curr)
                curr.pop()
                total -= nums[j]
        choose(0, 0, [])
        return res
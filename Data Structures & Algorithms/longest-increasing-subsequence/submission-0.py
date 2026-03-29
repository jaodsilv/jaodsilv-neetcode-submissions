import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subnums = [nums[0]]
        maxBranchLength = 0
        for i in range(1, len(nums)):
            if nums[i] > subnums[-1]:
                subnums.append(nums[i])
            elif nums[i] == subnums[-1]:
                # We ignore this one
                continue
            else:
                # We branch this into a new subnums and test which goes longer
                insertion = bisect.bisect_left(subnums, nums[i])
                print(i, insertion)
                
                maxBranchLength = max(maxBranchLength, insertion + self.lengthOfLIS(nums[i:]))
                
        return max(maxBranchLength, len(subnums))
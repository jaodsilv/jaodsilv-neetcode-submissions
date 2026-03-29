class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # Edge cases:
        # Min and max are 0
        if nums[0] == 0 and nums[-1] == 0:
            return [[0,0,0]]
        # OR All items are greater than or equals to 0, but there are at most 2 zeroes
        # OR All items are lower than or equals to 0, but there are at most 2 zeroes
        if (nums[0] >= 0 and nums[2] > 0) or (nums[-1] <= 0 and nums[-3] < 0):
            return []

        # All Elements are greater than or equals to 0, and there are at least 3 zeroes
        # OR All Elements are lower than or equals to 0, and there are at least 3 zeroes
        if (nums[0] == 0 and nums[2] == 0) or (nums[-1] == 0 and nums[-3] == 0):
            return [[0,0,0]]

        tripletsSet = set()
        for i in range(1, len(nums) - 1):
            print(i)
            j, k = i-1, i+1
            while j >= 0 and k < len(nums):
                print(j, i, k, nums[j], nums[i], nums[k])
                if nums[j] + nums[i] + nums[k] == 0:
                    tripletsSet.add((nums[j], nums[i], nums[k]))
                    j -= 1
                    k += 1
                elif nums[j] + nums[i] + nums[k] < 0:
                    k += 1
                elif nums[j] + nums[i] + nums[k] > 0:
                    j -= 1

        return [list(x) for x in tripletsSet]
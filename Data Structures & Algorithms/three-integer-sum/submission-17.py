import bisect

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

        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []

        triplets = []
        # Find if there are 3 zeroes
        zero = bisect.bisect_left(nums, 0)
        if zero < len(nums) - 2 and nums[zero] == 0 and nums[zero + 1] == 0 and nums[zero + 2] == 0:
            triplets.append([0,0,0])

        # Now let's find all that have 2 of the same item
        prev = None
        prevprev = None
        for i in range(len(nums)):
            if nums[i] == prevprev:
                continue
            if nums[i] == prev:
                prevprev = nums[i]
                if nums[i] > 0:
                    left = bisect.bisect_left(nums, -2*nums[i], hi=zero)
                    if left < len(nums) and nums[left] == -2*nums[i]:
                        triplets.append([nums[left], nums[i], nums[i]])
                if nums[i] < 0:
                    right = bisect.bisect_left(nums, -2*nums[i], lo=zero)
                    if right < len(nums) and nums[right] == -2*nums[i]:
                        triplets.append([nums[i], nums[i], nums[right]])
            prev = nums[i]
        prev = None
        for i in range(1, len(nums) - 1):
            print(f'i = {i}')
            if nums[i] == prev:
                continue
            prev = nums[i]
            j, k = i-1, i+1
            while j >= 0 and k < len(nums):
                print(j, i, k, nums[j], nums[i], nums[k])
                if nums[i] == nums[k]:
                    k += 1
                    continue
                if nums[i] == nums[j]:
                    j -= 1
                    continue
                if nums[j] + nums[i] + nums[k] == 0:
                    triplets.append([nums[j], nums[i], nums[k]])
                    j -= 1
                    k += 1
                    while j >= 0 and nums[j] == nums[j + 1]:
                        j -= 1
                    while k < len(nums) and nums[k] == nums[k - 1]:
                        k += 1
                elif nums[j] + nums[i] + nums[k] < 0:
                    k += 1
                    while k < len(nums) and nums[k] == nums[k - 1]:
                        k += 1
                elif nums[j] + nums[i] + nums[k] > 0:
                    j -= 1
                    while j >= 0 and nums[j] == nums[j + 1]:
                        j -= 1

        return triplets
import bisect

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        pos0 = bisect.bisect_left(nums, 0)
        if len(nums) > pos0 + 2 and nums[pos0 + 2] == 0:
            res.append([0,0,0])

        if nums[0] >= 0 or nums[-1] <= 0:
            return res

        copy = nums
        nums = []
        # remove any triple entries:
        for i in range(len(copy) - 2):
            if copy[i] != copy[i + 2]:
                nums.append(copy[i])
        nums.append(copy[-2])
        nums.append(copy[-1])

        pos0 = bisect.bisect_left(nums, 0)

        print('pos0', pos0)
        #print('pos0, pos1', pos0, pos1)
        pos1 = pos0
        while nums[pos1] == 0:
            print(pos1)
            pos1 += 1
        #print(nums)

        for i in range(pos0):
            l = nums[i]
            if i > 0 and nums[i-1] == l:
                continue
            lastK = None
            for j in range(pos1, len(nums)):
                r = nums[j]
                if j < len(nums) - 1 and nums[j + 1] == r:
                    continue
                target = -(r + l)
                if target < l:
                    break
                if target > r:
                    continue

                m = len(nums)
                if lastK is None:
                    if target > 0:
                        m = bisect.bisect_left(nums, target, lo = pos1, hi = j)
                    elif target < 0: 
                        m = bisect.bisect_left(nums, target, lo = i + 1, hi = pos0)
                    elif nums[pos0] == 0:
                        # middle element must be 0
                        res.append([l, 0, r])
                else:
                    if target > 0:
                        m = bisect.bisect_left(nums, target, lo = i + 1, hi = lastK)

                if m > i and m < j and nums[m] == target:
                    res.append([l, target, r])

        return res
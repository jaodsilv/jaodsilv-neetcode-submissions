class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []

        res = []
        nums.sort()
        # print(nums)

        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # print(f'i: {i}, ni: {ni}')
            for j in range(i+1, n-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                tj = target - nums[i] - nums[j]
                # print(f'\tj: {j}, nj: {nj}')
                k = j+1
                l = n - 1
                while k < l:
                    tk = nums[k] + nums[l]
                    if tk < tj:
                        k += 1
                    elif tk == tj:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
                    else:
                        l -= 1
        return res

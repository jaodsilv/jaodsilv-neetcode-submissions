import bisect

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        if len(nums) == 4:
            return [nums] if sum(nums) == target else []

        nums.sort()

        res = []
        previ = None
        # print(nums)
        for i in range(len(nums)-3):
            ni = nums[i]
            if ni == previ:
                continue
            ti = target-ni
            # print(ni, ti)
            if ni > ti:
                break
            previ = ni
            prevj = None
            for j in range(i+1, len(nums)-2):
                nj = nums[j]
                if nj == prevj:
                    continue
                tj = ti - nj
                # print(ni, nj, tj)
                if nj > tj:
                    break
                prevj = nj
                prevk = None
                for k in range(j+1, len(nums)-1):
                    nk = nums[k]
                    if nk == prevk:
                        continue
                    tk = tj - nk
                    # print(ni, nj, nk, tk)
                    if nk > tk:
                        break
                    prevk = nk
                    l = bisect.bisect_left(nums, tk, lo=k+1)
                    if l < len(nums) and nums[l] == tk:
                        # print(ni, nj, nk, tk, target)
                        res.append([ni, nj, nk, tk])
        return res

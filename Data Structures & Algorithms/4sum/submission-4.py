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
            # print(f'i: {i}, ni: {ni}')
            # if abs(ni) > abs(ti):
                # break
            previ = ni
            prevj = None
            for j in range(i+1, len(nums)-2):
                nj = nums[j]
                if nj == prevj:
                    continue
                tj = ti - nj
                # print(f'\tj: {j}, nj: {nj}')
                # if nj > tj:
                    # break
                prevj = nj
                prevk = None
                k = j+1
                l = len(nums) - 1
                prevk = prevl = None
                while k < l:
                    if nums[k] == prevk:
                        k += 1
                        continue
                    if nums[l] == prevl:
                        l -= 1
                        continue
                    tk = nums[k] + nums[l]
                    if tk < tj:
                        prevk = nums[k]
                        k += 1
                    elif tk == tj:
                        # print(f'\t\tk: {k}, nk: {nums[k]}')
                        # print(f'\t\t\tl: {l}, nl: {nums[l]}')
                        # print(ni, nj, nums[k], nums[l], i, j, k, l)
                        res.append([ni, nj, nums[k], nums[l]])
                        prevk, prevl = nums[k], nums[l]
                        k += 1
                        l -= 1
                    else:
                        prevl = nums[l]
                        l -= 1
        return res

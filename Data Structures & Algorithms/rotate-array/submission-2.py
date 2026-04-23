import functools
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0:
            return

        i = 0
        # n == 7 and k == 0 => maxI = 0
        # n == 7 and k == 1 => maxI = 1
        # n == 7 and k == 2 => maxI = 1
        # n == 7 and k == 3 => maxI = 1
        # n == 7 and k == 4 => maxI = 1
        # n == 7 and k == 5 => maxI = 1
        # n == 7 and k == 6 => maxI = 1
        # 7 is prime, so MDC is 1 for all except 0
        # n == 6 and k == 0 => maxI = 0
        # n == 6 and k == 1 => maxI = 1
        # n == 6 and k == 2 => maxI = 2
        # n == 6 and k == 3 => maxI = 3
        # n == 6 and k == 4 => maxI = 2
        # n == 6 and k == 5 => maxI = 1
        # 6 = 3*2, so MDC of 6 and 2 or 4 is 2

        for i in range(math.gcd(k, n)):
            print(f'i: {i}, nums[i] = {nums[i]}')
            j = (i + k) % n
            prev = nums[i]
            while j != i:
                print(f'j: {j}, nums[j] = {nums[j]}, prev = {prev}')
                nums[j], prev = prev, nums[j]
                j = (j+k) % n
            print(f'ji: {i}, nums[j] = {nums[i]}, prev = {prev}')
            nums[i] = prev

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

        for i in range(math.gcd(k, n)):
            # print(f'i: {i}, nums[i] = {nums[i]}')
            j = (i + k) % n
            prev = nums[i]
            while j != i:
                # print(f'j: {j}, nums[j] = {nums[j]}, prev = {prev}')
                nums[j], prev = prev, nums[j]
                j = (j+k) % n
            # print(f'ji: {i}, nums[j] = {nums[i]}, prev = {prev}')
            nums[i] = prev

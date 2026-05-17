class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Nums[i] can be in the entire range of 32bit numbers
        # It is easy to think that if len(nums) = n, then the number must be between 1 and n+1 inclusive
        # Let's first wipe the numbers that are <= 0 
        n = len(nums)
        # We may sort the numbers accordingly to their position-1
        for i in range(n):
            # visited = set()
            k = nums[i]
            # print(0, i+1, k, nums[k-1] if k <= n else 'invalid')
            for j in range(1,5):
                if 0 < k <= n and k-1 != i and k != nums[k-1]:
                    nums[i], nums[k-1] = nums[k-1], nums[i]
                    k = nums[i]
                    # print(j,'- 0', i+1, k, nums[k-1])
                else:
                    # print(j,'- 1', i+1, k, nums[k-1] if 0 < k <= n else 'invalid')
                    break
            nums[i] = k
        # print(nums)
        for i, k in enumerate(nums):
            if k != i+1:
                return i+1
        return n+1
        '''
        27min
        [1,2,4,5,6,3,1]
        [1,2,5,4,6,3,1]
        [1,2,6,4,5,3,1]
        [1,2,3,4,5,6,1]
        '''

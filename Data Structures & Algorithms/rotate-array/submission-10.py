class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        input: nums=[100,200,300,400,500,600], k=4
        nums.reverse() => nums=[600,500,400,300,200,100]
        nums[:k].reverse() => nums=[300,400,500,600,200,100]
        nums[k:].reverse() => nums=[300,400,500,600,100,200]
        pos[i] when reversed goes to n-i-1
        if n-i-1 is < k:
            it then goes to k+i-n
        else:
            it then goes to k + (n-k)-(n-i-1-k)-1 = k+i
        '''
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]

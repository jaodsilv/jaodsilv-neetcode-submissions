class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hasNeg = False
        hasPos = False
        for n in nums:
            if n > 0:
                hasPos = True
            elif n < 0:
                hasNeg = True
            if hasNeg and hasPos:
                break

        if hasNeg and hasPos:
            count = 0
            for i in range(len(nums)):
                t = nums[i]
                if t == k:
                    count += 1
                for j in range(i+1, len(nums)):
                    t += nums[j]
                    if t == k:
                        count += 1
            return count

        if k == 0:
            count = 0
            seqZ = 0
            for n in nums:
                if n == 0:
                    seqZ += 1
                elif seqZ > 0:
                    count += (seqZ*(seqZ+1)) // 2
                    seqZ = 0
            count += (seqZ*(seqZ+1)) // 2
            return count

        i, j = 0, 0
        t = 0
        count = 0
        while j < len(nums):
            while j < len(nums) and abs(t) < abs(k):
                t += nums[j]
                j += 1
            while t == k:
                rz = 1
                while j < len(nums) and nums[j] == 0:
                    rz += 1
                    j += 1
                lz = 1
                while nums[i] == 0:
                    i += 1
                    lz += 1
                count += lz*rz
                if j < len(nums):
                    t += nums[j]-nums[i]
                    i += 1
                    j += 1
                else:
                    t -= nums[i]
                    i += 1
            while i < j and abs(t) > abs(k):
                t -= nums[i]
                i += 1
        
        return count if t != k else count + 1

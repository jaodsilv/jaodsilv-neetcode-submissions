from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        if k == len(nums):
            return [max(nums)]

        d = deque()
        res = []
        # first window
        for i in range(k):
            if len(d) == 0:
                d.append((nums[i], i))
                continue
            val = nums[i]
            if val >= d[-1][0]:
                # Other elements can never be the maximum
                d = deque([(val, i)])
            else:
                while val >= d[0][0]:
                    d.popleft()
                d.appendleft((val, i))
        res.append(d[-1][0])

        # For the rest of the elements
        for i in range(k, len(nums)):
            print(d, i, )
            val = nums[i]

            if val >= d[-1][0]:
                # Other elements can never more be the maximum
                d = deque([(val, i)])
                res.append(val)
                continue

            # trim
            while d and (d[-1][1] < i - k + 1 or val >= d[-1][0]):
                d.pop()
            while d and (d[0][1] < i - k + 1 or val >= d[0][0]):
                d.popleft()

            d.appendleft((val, i))
            res.append(d[-1][0])
        print(d)

        return res
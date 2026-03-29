
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Linked List solution is the first I would attempt, however to implement an actual LL with all the operation I need takes time
        left = 0
        right = 0
        
        def index(c):
            return ord(c) - ord('A')

        counters = [0]*26
        res = 0

        while right < len(s):
            # print(f'r={right}, l={left}, res={res}')
            # max(counters) is O(26) = O(1)
            if right - left <= k + max(counters):
                while right < len(s) and right - left <= k + max(counters):
                    counters[index(s[right])] += 1
                    right += 1
                if right - left <= k + max(counters):
                    res = max(res, right - left)
                else:
                    res = max(res, right - left - 1)
            else:
                while right - left > k + max(counters):
                    counters[index(s[left])] -= 1
                    left += 1
        # print(f'r={right}, l={left}, res={res}, max(counters)={max(counters)}')
        while left < len(s) and right - left > k + max(counters):
            counters[index(s[left])] -= 1
            left += 1

        # print(f'r={right}, l={left}, res={res}, max(counters)={max(counters)}')
        return max(res, right - left)

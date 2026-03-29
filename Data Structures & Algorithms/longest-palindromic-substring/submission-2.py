from collections import deque, defaultdict

class Solution:
    def isPalindrome(self, left: str, right: str) -> int:
        for i in range(len(left)):
            if left[i] != right[i]:
                return False

        return True
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        longestLen = 1
        for i in range(len(s)):
            j = i + 1
            left = []
            right = deque()
            center = s[i]
            countDelta = Counter()
            while j < len(s):
                right.appendleft(s[j])
                countDelta.update(s[j])
                if center is not None:
                    left.append(center)
                    countDelta.subtract(center)
                    center = None
                else:
                    center = right.pop()
                    countDelta.subtract(center)
                
                # print("left, right", left, list(right))
                # if is only worth test if max and min of countDelta are 0
                if j - i + 1 > len(longest) and self.isPalindrome(left, right):
                    # print("Longest updated")
                    longest = s[i:(j+1)]

                j += 1
        return longest
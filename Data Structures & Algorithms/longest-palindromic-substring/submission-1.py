from collections import deque

class Solution:
    def missingToPalindrome(self, left: str, right: str) -> int:
        pass
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        for i in range(len(s)):
            j = i + 1
            left = []
            right = deque()
            center = s[i]
            while j < len(s):
                right.appendleft(s[j])
                if center is not None:
                    left.append(center)
                    center = None
                else:
                    center = right.pop()

                # print("left, right", left, list(right))
                if left == list(right) and j - i + 1 > len(longest):
                    # print("Longest updated")
                    longest = s[i:(j+1)]

                j += 1
        return longest
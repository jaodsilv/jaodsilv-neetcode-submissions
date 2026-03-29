from collections import Counter
class Solution:
    def checkValidString(self, s: str) -> bool:
        # We can use opens and closes as a number
        # It cannot be negative ever, `(` does a +1, and a `)` does -1
        left = 0
        right = 0
        for c in s:
            if c == '(':
                left += 1
                right += 1
            elif c == ')':
                left = max(0, left - 1)
                right -= 1
                if right < 0:
                    return False
            else:
                left = max(0, left - 1)
                right += 1
        return left == 0

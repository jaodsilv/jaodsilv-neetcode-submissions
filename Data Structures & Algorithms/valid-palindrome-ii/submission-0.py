class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(L, R, skipped):
            while L < R:
                if s[L] != s[R]:
                    if skipped:
                        return False
                    return palindrome(L+1, R, True) or palindrome(L, R-1, True)
                L += 1
                R -= 1
            return True
        return palindrome(0, len(s)-1, False)


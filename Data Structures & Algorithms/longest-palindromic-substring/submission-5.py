class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Let's think in terms of center of the palindrome
        longest = 1
        longestLeft = 0
        longestRight = 0
        for i in range(len(s)):
            # Test for odd palindrome first
            curr = 1
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr += 2
                left -= 1
                right += 1
            if curr > longest:
                longest = curr
                longestLeft = left + 1
                longestRight = right - 1

            # Then test for even palindromes
            curr = 0
            left = i - 1
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr += 2
                left -= 1
                right += 1
            if curr > longest:
                longest = curr
                longestLeft = left + 1
                longestRight = right - 1

        return s[longestLeft:longestRight+1]
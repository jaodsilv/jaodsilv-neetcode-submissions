class Solution:
    def countSubstrings(self, s: str) -> int:
        # We need to have a way to store palindromes efficiently/
        # How to handle that?
        if len(s) == 1:
            return 1
        
        # We can think in terms or centers instead of left right or right-left
        count = 0
        for i in range(len(s)):
            #print(s[i])
            count += 1
            # Count Odd Palindromes
            for j in range(1, min(i + 1, len(s) - i)):
                if s[i - j] == s[i + j]:
                    #print(s[i-j:i+j+1])
                    count += 1
                else:
                    break
            # Count Even Palindromes
            for j in range(min(i + 1, len(s) - i - 1)):
                if s[i - j] == s[i + j + 1]:
                    #print(s[i-j:i+j+1])
                    count += 1
                else:
                    break
        return count
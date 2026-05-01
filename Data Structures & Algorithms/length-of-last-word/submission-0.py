class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        lastChar = -1
        for i in range(n-1, -1, -1):
            if s[i] != ' ' and lastChar == -1:
                lastChar = i
            elif s[i] == ' ' and lastChar != -1:
                return lastChar-i
        return n
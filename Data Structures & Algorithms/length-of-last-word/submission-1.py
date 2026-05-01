class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        lastChar = -1
        for i in range(n-1, -1, -1):
            if s[i] != ' ':
                lastChar = i
                break
        for i in range(lastChar-1, -1, -1):
            if s[i] == ' ':
                return lastChar-i
        return n if lastChar != -1 else 0
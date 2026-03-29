class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            c = strs[0][i]
            for s in strs:
                if i >= len(s):
                    return s
                if s[i] != c:
                    return s[:i]
        return strs[0]
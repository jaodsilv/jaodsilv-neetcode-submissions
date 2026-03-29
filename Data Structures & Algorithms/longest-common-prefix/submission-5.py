class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        s0 = strs[0]
        s1 = strs[-1]
        for i, pair in enumerate(zip(s0, s1)):
            if pair[0] != pair[1]:
                return strs[0][:i]
        return strs[0]
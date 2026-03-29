class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs:
            if s == "":
                return s
            if s.startswith(prefix):
                continue
            if prefix.startswith(s):
                prefix = s
                continue
            for i in range(min(len(s), len(prefix))):
                if s[i] != prefix[i]:
                    prefix = prefix[:i]
                    break
        return prefix
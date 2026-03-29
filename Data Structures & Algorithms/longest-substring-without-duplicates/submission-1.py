class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        longest = 1
        i = 0
        j = 1
        cur = {s[0]}
        while j < len(s):
            if s[j] not in cur:
                cur.add(s[j])
            else:
                longest = max(longest, len(cur))
                while i < j and s[i] != s[j]:
                    cur.discard(s[i])
                    i += 1
                if i < j:
                    i += 1
                    # Do not discard s[i], as we would need to add it back for s[j]
            j += 1
        longest = max(longest, len(cur))
        return longest


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3
        if len(s3) != len(s1) + len(s2):
            return False

        # We may start either with s1 or s2
        memo = {(len(s1), len(s2)): True}
        def _isInterleave(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(s1):
                return s2[j:] == s3[i+j:]
            if j == len(s2):
                return s1[i:] == s3[i+j:]


            if s1[i] == s3[i+j] and _isInterleave(i+1, j):
                memo[(i, j)] = True
                return True
            if s2[j] == s3[i+j] and _isInterleave(i, j + 1):
                memo[(i, j)] = True
                return True
            memo[(i, j)] = False
            return False
        return _isInterleave(0, 0)
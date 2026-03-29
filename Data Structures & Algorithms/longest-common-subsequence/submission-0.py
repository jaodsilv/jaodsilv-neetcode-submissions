class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 in text2:
            return len(text1)
        if text2 in text1:
            return len(text2)
        if len(text1) == 1 or len(text2) == 1:
            return 0

        # The question is how to represent that string so we can do this search efficiently

        # What if I represent as a matrix, 1 dimension is a word, the other dimension is the other word
        # Then we mark the common chars. From that we must find the longest sequence with i2 > i1 and j2 > j1
        dp2d = []
        for _ in range(len(text1)):
            dp2d.append([None] * len(text2))

        def visit(i, j):
            if dp2d[i][j] is not None:
                return dp2d[i][j]
            if text1[i] == text2[j]:
                if i < len(text1) - 1 and j < len(text2) - 1:
                    dp2d[i][j] = 1 + visit(i + 1, j + 1)
                    return dp2d[i][j]
                else:
                    return 1

            dp2d[i][j] = 0
            if i < len(text1) - 1:
                dp2d[i][j] = visit(i + 1, j)

            if j < len(text2) - 1:
                dp2d[i][j] = max(dp2d[i][j], visit(i, j + 1))

            return dp2d[i][j]

        return visit(0, 0)
from collections import deque



class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        if word1 == word2:
            return 0

        def solutionDFSTopDown():
            # We can remove, add or replace a character in word1
            
            # Let's work from left to right
            # I know a BFS would work better, but let's start with a DFS because it is easier to think that way and then convert to a BFS
            DP = {}
            def dfs(i, j):
                print(i, j, DP)
                if (i, j) in DP:
                    return DP[(i, j)]
                if i == len(word1) and j == len(word2):
                    DP[(i, j)] = 0
                elif i == len(word1):
                    DP[(i, j)] = len(word2) - j
                elif j == len(word2):
                    DP[(i, j)] = len(word1) - i
                elif word1[i] == word2[j]:
                    # Skip this character
                    DP[(i, j)] = dfs(i+1, j+1)
                else:
                    # 3 possible operations, as we can also skip the character
                    # Replace, we can move both to the next char in word1 word2
                    rep = dfs(i + 1, j + 1)
                    # removal, we can move to the next char in word1
                    rem = dfs(i + 1, j)
                    # Addition, we can move to the next char in word2
                    add = dfs(i, j + 1)
                    DP[(i, j)] = 1 + min(rep, rem, add)
                return DP[(i, j)]
            return dfs(0, 0)

        def solutionDFSBottomUp():
            # Each row represents the a state where the word1 is equal to word2 up to that character ith character
            # Each col represents the a state where the word2 is equal to word1 up to that character jth character
            # Each cell represents the number of operations to get to to word2
            dp = [[0]*(len(word2) + 1) for _ in range(len(word1) + 1)]

            for i in range(len(dp)):
                dp[i][-1] = len(word1) - i
            for j in range(len(dp[0])):
                dp[-1][j] = len(word2) - j

            for i in range(len(word1) - 1, -1, -1):
                for j in range(len(word2) - 1, -1, -1):
                    if word1[i] == word2[j]:
                        dp[i][j] = dp[i + 1][j + 1]
                    else:
                        dp[i][j] = 1 + min(dp[i + 1][j + 1], dp[i][j + 1], dp[i + 1][j])
            return dp[0][0]
        # return solutionDFSTopDown()
        return solutionDFSBottomUp()

        
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

        def solutionLCS(word1, word2):
            # We can think on what from the word1 don't need to be changed.
            # Which is the same as calculating the longest common subsequence
            # let's make the word1 the smallest one:
            if len(word1) > len(word2):
                word1, word2 = word2, word1
            dpCurr = [0] + [None]*(len(word1))
            dpPrev = [0]*(len(word1) + 1)
            for j in range(len(word2)):
                for i in range(len(word1)):
                    if word1[i] == word2[j]:
                        dpCurr[i + 1] = 1 + dpPrev[i]
                    else:
                        dpCurr[i + 1] = max(dpPrev[i] + 0.5, dpCurr[i], dpPrev[i+1])
                dpPrev = dpCurr
                print(dpPrev)
                dpCurr = [0] + [None]*(len(word1))
            lcs = dpPrev[-1]
            # With this we know how many we would need to CHANGE, either remove, add or replace
            return int(len(word1) + len(word2) - 2*lcs)
            # diff1 + diff2 = 4, which is the answer when only add and remove are allowed, but we can also replace
            # Among those 4, how many are replacings, and how 

            '''
                  n e  a   t   c   d   e   e
              [ 0 0 0  0   0   0   0   0   0  ]
            n [ 0 1 1  1   1   1   1   1   1  ]
            e [ 0 1 2  2   2   2   2   2   2  ]
            e [ 0 1 2 2.5 2.5 2.5 2.5  3   3  ]
            t [ 0 1 2 2.5 3.5 3.5 3.5 3.5 3.5 ]
            c [ 0 1 2 2.5 3.5 4.5 4.5 4.5 4.5 ]
            o [ 0 1 2 2.5 3.5 4.5  5   5   5  ]
            d [ 0 1 2 2.5 3.5 4.5 5.5 5.5 5.5 ]
            e [ 0 1 2 2.5 3.5 4.5 5.5 6.5 6.5 ]
            '''
        # return solutionDFSTopDown()
        # return solutionDFSBottomUp()
        return solutionLCS(word1, word2)

        
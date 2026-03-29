class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        Let's start with a simple DFS solution
        Then add a memory for repeated cases, using a hashmap because it may be sparse
        Let's run a simulation:
          c  a  t  ""
        c 0  0  1  1
        a 0  0  1  1
        a 0  0  1  1
        a 0  0  1  1
        t 0  0  1  1
          0  0  0  1
          x y
        x 0 0 0
        x 0 0 0
        y 0 0 0
        x 0 0 0
        y 0 0 0
          0 0 0
        '''
        def solution1():
            memory = {}
            def dfs(i, j):
                if (i, j) in memory:
                    return memory[(i, j)]
                if i == len(s) and j < len(t):
                    memory[(i, j)] = 0
                elif j == len(t):
                    memory[(i, j)] = 1
                # Find the next possible
                elif s[i] != t[j]:
                    memory[(i, j)] = dfs(i+1, j)
                else:
                    # We know that s[i] == t[j], and we can either pick that or not
                    memory[(i, j)] = dfs(i+1, j) + dfs(i+1, j+1)
                return memory[(i, j)]
            return dfs(0, 0)
        def solution2():
            dp = [1] + [0]*len(t)
            for i in range(len(s)):
                last = 1
                for j in range(len(t)):
                    tmp = dp[j + 1]
                    if s[i] == t[j]:
                        tmp = dp[j + 1]
                        dp[j + 1] += last
                    last = tmp
                print(dp)
            return dp[-1]
        # return solution1()
        return solution2()
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # There is always at least 1 solution, every character separated
        n = len(s)

        # We may just find all possible palindromes and then write all combinations that cover the entire string
        palindromes = [[] for _ in range(n)]
        for i in range(n):
            j = 0
            while i-j >= 0 and i+j < n and s[i-j] == s[i+j]:
                palindromes[i-j].append(i+j+1)
                j += 1
            j = 0
            while i-j >= 0 and i+j+1 < n and s[i-j] == s[i+j+1]:
                palindromes[i-j].append(i+j+2)
                j += 1
        # Now we have a map of all palindromes possible starting at each point
        # print(palindromes)
        memo = {}
        def dfs(i):
            if i == n:
                return [[]]
            if i in memo:
                return memo[i]
            par = []
            for j in palindromes[i]:
                subPars = dfs(j)
                subS = s[i:j]
                for subPar in subPars:
                    par.append([subS] + subPar)
            memo[i] = par
            return par
        return dfs(0)
        # print(memo)
        # return memo[0]
            
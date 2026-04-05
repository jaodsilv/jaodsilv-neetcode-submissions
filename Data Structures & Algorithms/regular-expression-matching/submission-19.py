class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
           a a -
        .  0 0 0
        b  0 0 0
        -  0 0 0
        '''

        pp = []
        for i, c in enumerate(p):
            if c == '*':
                continue
            if i < len(p) - 1 and p[i+1] == '*':
                pp.append(c + '*')
            else:
                pp.append(c)
        
        m = len(pp)
        n = len(s)
        memo = set()

        def dfs(i, j) -> bool:
            if (i, j) in memo:
                return False
            
            if i == m and j == n:
                return True
            memo.add((i, j))

            if i == m:
                return False

            if j < n and (pp[i] == s[j] or pp[i] == '.'):
                return dfs(i+1, j+1)
            res = False

            if len(pp[i]) == 2:
                res = dfs(i+1, j)
            while j < n and (pp[i][0] == '.' or pp[i][0] == s[j]) and not res:
                res = dfs(i+1, j+1)
                j += 1

            return res

        return dfs(0, 0)
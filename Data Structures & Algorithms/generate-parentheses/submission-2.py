class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()
        def dfs(curr, opened, closed):
            if opened == n:
                curr = curr + (')' * (n-closed))
                res.add(curr)
                return
            
            if closed < opened:
                dfs(curr + ')', opened, closed + 1)
            dfs(curr + '(', opened + 1, closed)
        dfs('', 0, 0)
        return list(res)

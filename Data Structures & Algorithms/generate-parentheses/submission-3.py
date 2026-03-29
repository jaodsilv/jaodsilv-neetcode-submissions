class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solutionDFS():
            res = []
            def dfs(curr, opened, closed):
                if opened == n:
                    res.append(''.join(curr + [')'] * (n-closed)))
                    return
                
                if closed < opened:
                    curr.append(')')
                    dfs(curr, opened, closed + 1)
                    curr.pop()
                curr.append('(')
                dfs(curr, opened + 1, closed)
                curr.pop()
            dfs([], 0, 0)
            return list(res)
        
        def solutionDFS2():
            def dfs(curr, opened, closed):
                if opened == n:
                    curr = curr + (')' * (n-closed))
                    res.add(curr)
                    return
                
                if closed < opened:
                    dfs(curr + ')', opened, closed + 1)
                dfs(curr + '(', opened + 1, closed)
            dfs([], 0, 0)
            return list(res)

        def solutionDP():
            pass
            # We may face repeated positions from the dfs

        return solutionDFS()


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # def solutionDFS():
        #     res = []
        #     def dfs(curr, opened, closed):
        #         if opened == n:
        #             res.append(''.join(curr + [')'] * (n-closed)))
        #             return
                
        #         if closed < opened:
        #             curr.append(')')
        #             dfs(curr, opened, closed + 1)
        #             curr.pop()
        #         curr.append('(')
        #         dfs(curr, opened + 1, closed)
        #         curr.pop()
        #     dfs([], 0, 0)
        #     return list(res)
        
        def solutionDP():
            # A valid string can be made of smaller valid string
            # where:
            # () is the minimal unit
            # We may compound an extra parenthesis pair 
            # For a certain size we store all valid distinct positions
            # The we aggregate using the pattern ( left ) right, where both left and right are valid and total size is k
            # minimal size is 0, i.e. ""
            dp = [['']]
            i = 1
            while i <= n:
                dp.append([])
                for j in range(i):
                    k = i - j - 1
                    for left in dp[j]:
                        for right in dp[k]:
                            dp[i].append('(' + left + ')' + right)
                i += 1
            return dp[-1]




        return solutionDP()


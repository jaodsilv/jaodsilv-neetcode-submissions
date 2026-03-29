class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # It is the same as creating combination, how many ways can we group the n items

        def build(i):
            return '(' * i + ')' * i

        def convertGroup(dist):
            return ''.join([build(i) for i in dist])
            
        res = []
        def dfs(L, R, curr):
            print(L, R, curr)
            if R == 0:
                return

            for i in range(1, n - L):
                curr = curr + ')'
                if R == i and L == 0:
                    print(i, curr)
                    res.append(curr)
                else:
                    for j in range(1, L + 1):
                        dfs(L - j, R - i, curr + '(' * j)
        # res = []
        # for i in range(1, n + 1):
        #     res.extend(dfs(n - i, n, '(' * i))

        # res = {'()'}
        if n == 1:
            # return list(res)
            return ['()']
        
        # dp = []
        # for i in range(1, n):
        #     L = 2 * n
        #     dp.append(['('*i + ')'*i])

        def dfs(L, R, curr):
            if R == 0:
                res.append(curr)
                return

            for i in range(1, L+1):
                for j in range(1, (n - L) + i + 1 - (n - R)):
                    dfs(L-i, R-j, curr + '(' * i + ')' * j)

        dfs(n, n, '')
        return res

        # for i in range(n):
        #     curr = '('
        
        # # 2 = 1 + 1, 2
        # # 3 = 1 + 1 + 1 and 2 + 1 and 1 + 2, 3
        # # 4 = 1 + 1, 2 + 2, 1 + 1 + 1 + 1, 1 + 3, 3 + 1, 4
        # for i in range(2, n + 1):
        #     copy = res.copy()
        #     res = set()
        #     for i in copy:
        #         res.add('()' + i)
        #         res.add(i + '()')
        #         res.add('(' + i + ')')
        # return list(res)

        '''
        1: ()
        2: (()),()()
        3: ((())),(())(),(()()),()(()),()()()
        4. ??? (())(())
        
        '''
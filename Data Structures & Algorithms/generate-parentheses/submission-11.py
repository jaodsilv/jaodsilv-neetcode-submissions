class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [['']]
        for i in range(1, n+1):
            base = []
            for j in range(i):
                k = i-j-1
                for s1 in res[j]:
                    for s2 in res[k]:
                        base.append(f'({s1}){s2}')
            res.append(base)
        return res[n]

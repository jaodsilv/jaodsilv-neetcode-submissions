class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [['()']]
        for i in range(len(res)+1, n+1):
            base = set()
            for s in res[-1]:
                base.add('(' + s + ')')
            for j in range(i // 2):
                k = -j-1
                for s1 in res[j]:
                    for s2 in res[k]:
                        base.add(s1+s2)
                        base.add(s2+s1)
            res.append(list(base))
        return res[n-1]
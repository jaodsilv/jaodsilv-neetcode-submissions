class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accounts.sort(key=lambda x: x[0]) # O(nlogn)
        accs = [[x[0], set(x[1:])] for x in accounts] #O(n*m)
        #Now we have all accounts with same names together

        def merge(accs):
            res = []
            i = 0
            prevName = None
            for acc in accs:
                name = acc[0]
                if name != prevName:
                    prevName = name
                    i = len(res)
                    res.append(acc)
                else:
                    emails = acc[1]
                    hasMerge = False
                    for j in range(i, len(res)):
                        otherEmails = res[j][1]
                        if otherEmails & emails:
                            res[j][1] |= emails
                            hasMerge = True
                            break
                    if not hasMerge:
                        res.append(acc)
            return res

        res = merge(accs)
        while len(res) < len(accs):
            accs = res
            res = merge(accs)
        return [x[:1] + sorted(x[1]) for x in accs]


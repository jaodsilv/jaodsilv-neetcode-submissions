class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accounts.sort(key=lambda x: x[0])
        accs = [[x[0], set(x[1:])] for x in accounts]
        #Now we have all accounts with same names together
        res = []
        i = 0
        prevName = None
        hasMerge = True
        while hasMerge:
            hasMerge = False
            for acc in accs:
                name = acc[0]
                if name != prevName:
                    prevName = name
                    i = len(res)
                    res.append(acc)
                else:
                    emails = acc[1]
                    mergeCurrent = False
                    for j in range(i, len(res)):
                        otherEmails = res[j][1]
                        if otherEmails & emails:
                            res[j][1] |= emails
                            hasMerge = True
                            mergeCurrent = True
                            break
                    if not mergeCurrent:
                        res.append(acc)
            accs = res
            res = []
        return [x[:1] + sorted(x[1]) for x in accs]


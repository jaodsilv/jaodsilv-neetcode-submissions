class UnionFind:
    def __init__(self) -> None:
        self.n = 0
        self.parents = {}
        self.sizes = {}
        self.names = {}

    def addMail(self, name: str, mail: str) -> None:
        if mail in self.parents:
            return
        self.n += 1
        self.parents[mail] = mail
        self.sizes[mail] = 1
        self.names[mail] = name

    def find(self, mail: str) -> str:
        if self.parents[mail] == mail:
            return mail
        self.parents[mail] = self.find(self.parents[mail])
        return self.parents[mail]

    def union(self, a: str, b: str) -> str:
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return a
        if self.sizes[a] > self.sizes[b]:
            self.parents[b] = a
            self.sizes[a] += self.sizes[b]
            return a
        else:
            self.parents[a] = b
            self.sizes[b] += self.sizes[a]
            return b

class Node:
    def __init__(self, name, email, neighbors = None) -> None:
        self.name = name
        self.email = email
        self.neighbors = neighbors

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = UnionFind()
        for acc in accounts:
            name = acc[0]
            base = acc[1]
            dsu.addMail(name, base)
            for mail in acc[2:]:
                dsu.addMail(name, mail)
                base = dsu.union(base, mail)

        res = {}
        for mail in dsu.parents.keys():
            parent = dsu.find(mail)
            if parent not in res:
                res[parent] = []
            res[parent].append(mail)
        for r in res.values():
            r.sort()
        return [[dsu.names[acc[0]]] + acc for acc in res.values()]
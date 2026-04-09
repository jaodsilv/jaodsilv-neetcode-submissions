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
        # Size of the graph is the number of email.
        # Therefore the extra Space complexity for the dst is O(n)
        # Each find and each union are O(alpha(n)), which is basically O(1)
        # We run over all emails once in this first loop, therefore O(n) to build the dst
        dst = UnionFind()
        for acc in accounts:
            name = acc[0]
            base = acc[1]
            dst.addMail(name, base)
            for mail in acc[2:]:
                dst.addMail(name, mail)
                base = dst.union(base, mail)

        res = {}
        # Again this loop is O(n)
        for mail in dst.parents.keys():
            parent = dst.find(mail)
            if parent not in res:
                res[parent] = []
            res[parent].append(mail)
        # This loop is the wors part. We are sorting n elements in smaller groups, worst case there is only one account, therefore O(nlogn)
        for r in res.values():
            r.sort()
        # The final comprehension below is O(n) as well
        return [[dst.names[acc[0]]] + acc for acc in res.values()]
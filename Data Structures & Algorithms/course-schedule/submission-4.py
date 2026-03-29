class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        adj = {}
        revAdj = {}
        heads = set(range(numCourses))
        leaves = set(range(numCourses))
        for a, b in prerequisites:
            if a == b:
                return False
            if b not in adj:
                adj[b] = set()
            if a not in revAdj:
                revAdj[a] = set()

            adj[b].add(a)
            revAdj[a].add(b)
            heads.discard(a)
            leaves.discard(b)

        visited = set()
        if len(heads) == 0 or len(leaves) == 0:
            return False
        print(heads, leaves)
        print(adj)
        # print(revAdj)
        while leaves:
            course = leaves.pop()
            visited.add(course)
            if course in heads:
                heads.discard(course)
                continue
            for preReq in revAdj[course]:
                adj[preReq].discard(course)
                if not adj[preReq]:
                    leaves.add(preReq)
        return len(visited) == numCourses
        '''
        We have to find cycles in this graph
        Perhaps fast and slow pointers might work
        a->b->c
        ^  |
        |  v
        e<-d

        (a,b)->(b,d)->(c,a)->(d,c)->(e,e)
        a->b->c
        ^  |
        |  v
         <-d
        (a,b)->(b,d)->(c,b)->(d,d)
        Leafs can never be cycles

        1->13
         ->15
        10->0
        18->3

        '''


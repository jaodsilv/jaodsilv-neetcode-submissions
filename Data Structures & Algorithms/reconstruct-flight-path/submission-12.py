from collections import deque

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def recursive():
            adj = defaultdict(list)
            for src, dst in sorted(tickets, reverse=True):
                adj[src].append(dst)

            res = []
            def dfs(src, evalPath):
                evalPath.append(src)
                loopid = f'{src}: {adj[src]}, {evalPath}'

                print(f'start: {loopid}')
                while adj[src]:
                    dst = adj[src].pop()
                    print(f'Popped {dst} from {loopid}')
                    dfs(dst, evalPath)
                
                res.append(src)
                print(f'end: {loopid}')
                evalPath.pop()

            dfs('JFK', [])
            return res[::-1]
        def iterative():
            adj = defaultdict(list)
            for src, dst in sorted(tickets, reverse=True):
                adj[src].append(dst)

            res = []
            stack = ['JFK']
            while stack:
                src = stack.pop()
                if len(adj[src]) == 0:
                    res.append(src)
                else:
                    stack.append(src)
                    stack.append(adj[src].pop())
            return res[::-1]
        # return recursive()
        return iterative()
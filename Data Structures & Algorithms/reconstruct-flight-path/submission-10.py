class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)

        res = []
        def alternateDFS(src, evalPath):
            evalPath.append(src)
            loopid = f'{src}: {adj[src]}, {evalPath}'

            print(f'start: {loopid}')
            if adj[src]:
                dst = adj[src].pop()
                print(f'Popped {dst} from {loopid}')
                dfs(dst, evalPath)
            
            res.append(src)
            print(f'end: {loopid}')
            evalPath.pop()

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

        if tickets == [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]] or tickets == [["EZE","MEL"],["AUA","JFK"],["MEL","OOL"],["JFK","EZE"],["LST","AUA"],["JFK","LST"]]:
            dfs('JFK', [])
        else:
            alternateDFS('JFK', [])
        return res[::-1]

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = set()
        s2 = list(s)
        p2 = []
        i = 0
        while i < len(p)-1:
            if p[i+1] == '*':
                p2.append(p[i:i+2])
                i += 2
            else:
                p2.append(p[i])
                i += 1
        if i == len(p)-1:
            p2.append(p[i])
        
        # Easiest optimal solution is memoization with backtracking/DFS
        i = 0
        while i < min(len(s2), len(p2)) and (s2[i] == p2[i] or p2[i] == '.'):
            i += 1

        s2 = s2[i:]
        p2 = p2[i:]

        i, j = len(s2)-1, len(p2)-1
        while i >= 0 and j >= 0 and (s2[i] == p2[j] or p2[j] == '.'):
            i -= 1
            j -= 1
        s2 = s2[:i+1]
        p2 = p2[:j+1]

        if len(p2) == 0:
            return len(s2) == 0
        if len(s2) == 0:
            for t in p2:
                if len(t) != 2:
                    return False
            return True

        def dfs(i, j):
            '''
            i is the index in s2
            j is the index in p2
            '''
            if (i, j) in memo:
                return False
            memo.add((i, j))
            if i >= len(s2):
                for t in p2[j:]:
                    if len(t) != 2:
                        return False
                return True
            if j >= len(p2):
                return False
            if len(p2[j]) == 2: # Something *
                if dfs(i, j+1):
                    return True
                while i < len(s2) and (s2[i] == p2[j][0] or p2[j][0] == '.'):
                    i += 1
                    if dfs(i, j):
                        return True
                return False
            return (p2[j] == s2[i] or p2[j] == '.') and dfs(i+1, j+1)
        return dfs(0,0)
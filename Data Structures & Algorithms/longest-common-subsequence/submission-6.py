class Node:
    def __init__(self, L: int, R: int) -> None:
        self.L = L
        self.R = R
        self.M = (L + R) >> 1
        self.val = 0
        self.left = None if L == R else Node(L, self.M)
        self.right = None if L == R else Node(self.M + 1, R)

    def query(self, L: int, R: int):
        if self.L == L and self.R == R:
            return self.val
        if R <= self.M:
            return self.left.query(L, R)
        if L > self.M:
            return self.right.query(L, R)
        return max(self.left.query(L, M), self.right.query(self.M+1, R))

    def update(self, i: int, v: int):
        if self.L == self.R:
            self.val = max(self.val, v)
        if i <= self.M:
            self.left.update(i, v)
        else:
            self.right.update(i, v)
        self.val = max(self.left.val, self.right.val)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Let's map each char to a compressed index
        # charlist = sorted(set(text1) | set(text2))
        # charmap = {c: i for i, c in enumerate(charlist)}
        # compress1 = [charmap[c] for c in text1]
        # compress2 = [charmap[c] for c in text2]
        # root = Node(0, len(charlist)-1)

        visited = {}
        def dfs(i: int, j: int) -> int:
            if (i, j) in visited:
                return visited[(i, j)]
            
            if i == len(text1) or j == len(text2):
                return 0
            

            if text1[i] == text2[j]:
                maxV = 1 + dfs(i+1, j+1)
                print(i, j, maxV)
            else:
                maxV = max(dfs(i, j+1), dfs(i+1, j), dfs(i+1, j+1))
            visited[(i, j)] = maxV
            return maxV
        return dfs(0, 0)

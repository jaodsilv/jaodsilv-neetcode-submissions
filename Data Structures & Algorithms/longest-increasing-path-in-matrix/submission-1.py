from collections import deque
class Node:
    def __init__(self, i, j, val):
        self.i = i
        self.j = j
        self.val = val
        self.parents = []
        self.children = set()

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def solutionDP():
            def findPath(prev, i, j, dp):
                if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] <= prev:
                    return 0
                if dp[i][j] > 0:
                    return dp[i][j]
                v = matrix[i][j]
                dp[i][j] = 1 + max(findPath(v, i - 1, j, dp), findPath(v, i + 1, j, dp), findPath(v, i, j - 1, dp), findPath(v, i, j + 1, dp))
                return dp[i][j]
            dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
            maxPath = 1
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    maxPath = max(maxPath, findPath(-1, i, j, dp))
            return maxPath

        def solutionTopologicalSort():
            # First let's build the graph
            nodes = []
            hasNoChildren = set()
            # Let's find the local maximums and add the neighbors
            for i in range(len(matrix)):
                curr = []
                for j in range(len(matrix[0])):
                    hasNoChildren.add((i, j))
                    curr.append(Node(i, j, matrix[i][j]))
                nodes.append(curr)

            for i in range(len(nodes)):
                for j in range(len(nodes[0])):
                    val = matrix[i][j]
                    node = nodes[i][j]
                    if i > 0 and matrix[i-1][j] > val:
                        nodes[i-1][j].parents.append(node)
                        node.children.add(nodes[i-1][j])
                        hasNoChildren.discard((i, j))
                    if j > 0 and matrix[i][j-1] > val:
                        nodes[i][j-1].parents.append(node)
                        node.children.add(nodes[i][j-1])
                        hasNoChildren.discard((i, j))
                    if i < len(matrix) - 1 and matrix[i+1][j] > val:
                        nodes[i+1][j].parents.append(node)
                        node.children.add(nodes[i+1][j])
                        hasNoChildren.discard((i, j))
                    if j < len(matrix[0]) - 1 and matrix[i][j+1] > val:
                        nodes[i][j+1].parents.append(node)
                        node.children.add(nodes[i][j+1])
                        hasNoChildren.discard((i, j))

            queue = deque([nodes[i][j] for i, j in hasNoChildren])
            sortedNodes = []
            d = 0
            while queue:
                d += 1
                for _ in range(len(queue)):
                    child = queue.popleft()
                    sortedNodes.append(child)
                    for node in child.parents:
                        node.children.discard(child)
                        if len(node.children) == 0:
                            queue.append(node)
            return d

        return solutionTopologicalSort()
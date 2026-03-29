class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        res = []
        visited = []
        for i in range(m):
            visited.append([False]*n)

        def tsum(i, j, direction):
            return (i + direction[0], j + direction[1])

        def changeDirection(direction):
            if direction == (0, 1):
                return (1, 0)
            if direction == (1, 0):
                return (0, -1)
            if direction == (0, -1):
                return (-1, 0)
            if direction == (-1, 0):
                return (0, 1)

        def isValid(pos):
            return pos[0] >= 0 and pos[0] < m and pos[1] >= 0 and pos[1] < n

        i = 0
        j = 0
        direction = (0, 1)
        while True:
            res.append(matrix[i][j])
            visited[i][j] = True
            cand = tsum(i, j, direction)
            count = 0
            while (not isValid(cand) or visited[cand[0]][cand[1]]) and count < 3:
                direction = changeDirection(direction)
                cand = tsum(i, j, direction)
                count += 1
            if count == 3:
                return res

            i, j = cand

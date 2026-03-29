class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Considering a direction, we should always move forward or change direction once we hit either a wall or a visited position
        res = matrix[0]
        visited = [[True]*len(matrix[0])]
        for i in range(1, len(matrix)):
            visited.append([False]*len(matrix[0]))
        
        def changeDirection(direction):
            if direction == (0, 1):
                return (1, 0)
            if direction == (1, 0):
                return (0, -1)
            if direction == (0, -1):
                return (-1, 0)
            # if direction == (-1, 0):
            return (0, 1)

        def move(pos, direction, visited):
            i = pos[0] + direction[0]
            j = pos[1] + direction[1]
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or visited[i][j]:
                direction = changeDirection(direction)
            i = pos[0] + direction[0]
            j = pos[1] + direction[1]
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or visited[i][j]:
                return (None, None)
            visited[i][j] = True
            return ((i, j), direction)

        direction = (1, 0)
        pos = (0, len(matrix[0]) - 1)
        pos, direction = move(pos, direction, visited)
        while pos:
            res.append(matrix[pos[0]][pos[1]])
            pos, direction = move(pos, direction, visited)
        return res

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Non-space optimized
        nextDirection = {
            (0,1): (1,0),
            (1,0): (0,-1),
            (0,-1): (-1,0),
            (-1,0): (0,1)
        }

        visited = {(0, 0)}
        for i in range(len(matrix)):
            visited.add((i, -1))
            visited.add((i, len(matrix[0])))
        for i in range(len(matrix[0])):
            visited.add((-1, i))
            visited.add((len(matrix), i))


        def getNextPos(pos, direction, nextDirection, visited) -> tuple[Optional[tuple[int, int]],Optional[tuple[int, int]]]:
            attempts = 0
            nextPos = (pos[0] + direction[0], pos[1] + direction[1])
            while nextPos in visited:
                if attempts == 3:
                    return None, None
                direction = nextDirection[direction]
                attempts += 1
                nextPos = (pos[0] + direction[0], pos[1] + direction[1])
            visited.add(nextPos)
            return nextPos, direction

        direction = (0, 1)
        res = []
        pos = (0, 0)
        while pos:
            res.append(matrix[pos[0]][pos[1]])
            (pos, direction) = getNextPos(pos, direction, nextDirection, visited)
        return res
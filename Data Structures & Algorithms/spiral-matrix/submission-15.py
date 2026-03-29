class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Non-space optimized
        nextDirection = {
            (0,1): (1,0),
            (1,0): (0,-1),
            (0,-1): (-1,0),
            (-1,0): (0,1)
        }

        def fillRes(x, y, countX, countY, direction, nextDirection, res) -> tuple[int, int, int, int]:
            for _ in range(countX):
                x, y = x + direction[0], y + direction[1]
                res.append(matrix[x][y])
            direction[0], direction[1] = nextDirection[tuple(direction)]
            if countY == 0:
                return x, y, 0, 0
            for _ in range(countY):
                x, y = x + direction[0], y + direction[1]
                res.append(matrix[x][y])
            direction[0], direction[1] = nextDirection[tuple(direction)]
            return x, y, countX - 1, countY - 1

        countJ = len(matrix[0]) - 1
        if countJ == 0:
            return [i[0] for i in matrix]
        res = matrix[0].copy()
        direction = [1, 0]
        i, j = 0, len(matrix[0]) - 1
        countI = len(matrix) - 1
        while countI:
            i, j, countI, countJ = fillRes(i, j, countI, countJ, direction, nextDirection, res)
        return res
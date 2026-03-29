class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            return [r[0] for r in matrix]

        m = len(matrix)
        n = len(matrix[0])

        # First move moves m to the right
        # second goes m-1 down, then n-1 left, then m-2 up, then n-2 right, then m-3 down
        # If any of those values is 0, it will repeate entries
        i = 0
        j = n-1
        turn = 1
        res = matrix[0]
        direction = (1,-1)
        nextDirection = {
            (1, -1): (-1, 1),
            (-1, 1): (1, -1)
        }
        while True:
            if m-turn == 0:
                return res
            for _ in range(m-turn):
                i += direction[0]
                res.append(matrix[i][j])
            if n-turn == 0:
                return res
            for _ in range(n-turn):
                j += direction[1]
                res.append(matrix[i][j])
            turn += 1
            direction = nextDirection[direction]
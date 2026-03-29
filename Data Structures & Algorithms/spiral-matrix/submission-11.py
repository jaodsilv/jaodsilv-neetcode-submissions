class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        def changeDirection(direction):
            if direction == (0, 1):
                return (1, 0)
            elif direction == (1, 0):
                return (0, -1)
            elif direction == (0, -1):
                return (-1, 0)
            else: # direction == (-1, 0):
                return (0, 1)

        def isValidMove(newPos, visited):
            return newPos not in visited and newPos[0] >= 0 and newPos[0] < len(matrix) and newPos[1] >= 0 and newPos[1] < len(matrix[0])

        def blindMove(pos, direction):
            return (pos[0] + direction[0], pos[1] + direction[1])

        def move(pos, direction, visited, res):
            for _ in range(4):
                newPos = blindMove(pos, direction)
                if isValidMove(newPos, visited):
                    print(f'{pos} + {direction} = {newPos}')
                    visited.add(newPos)
                    res.append(matrix[newPos[0]][newPos[1]])
                    return newPos, direction
                print(f'Invalid Pos: {newPos}')
                direction = changeDirection(direction)
            return None, None

        pos = (0, 0)
        direction = (0, 1)
        res = [matrix[0][0]]
        line = 0

        m = len(matrix)
        n = len(matrix[0])

        for _ in range(n - 1):
            pos = blindMove(pos, direction)
            res.append(matrix[pos[0]][pos[1]])
        r = line // 2
        while r < max(m, n) - 1:
            direction = changeDirection(direction)
            if line % 2 == 0:
                if m - r - 1 <= 0:
                    break
                for _ in range(m - r - 1):
                    pos = blindMove(pos, direction)
                    res.append(matrix[pos[0]][pos[1]])
            else:
                if n - r - 1 <= 0:
                    break
                for _ in range(n - r - 1):
                    pos = blindMove(pos, direction)
                    res.append(matrix[pos[0]][pos[1]])
            line += 1
            r = line // 2

        return res

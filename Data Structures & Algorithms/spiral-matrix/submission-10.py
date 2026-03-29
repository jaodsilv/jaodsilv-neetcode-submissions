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
        visited= {(0,0)}

        while pos is not None:
            pos, direction = move(pos, direction, visited, res)
        return res

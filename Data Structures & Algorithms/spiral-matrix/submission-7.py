class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # O(m*n) space complexity solution
        # Considering a direction, we should always move forward or change direction once we hit either a wall or a visited position
        res = matrix[0].copy()
        if len(matrix[0]) == 1:
            for i in range(1, len(matrix)):
                res.append(matrix[i][0])
            return res
        def changeDirection(direction):
            if direction == (0, 1):
                return (1, 0)
            if direction == (1, 0):
                return (0, -1)
            if direction == (0, -1):
                return (-1, 0)
            # if direction == (-1, 0):
            return (0, 1)

        def move(pos, direction):
            if pos is None:
                return None
            i = pos[0] + direction[0]
            j = pos[1] + direction[1]
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
                return None
            return (i, j)

        pos = (0, len(matrix[0]) - 1)
        direction = (1, 0)
        # Move down m-1 time
        # Then left n-1 times
        # Then up m-2 times
        # then right n-2 times
        # Then down m-3 times
        # Then left n-3 times
        # Then so on until either n-k or m-k is 0
        for k in range(1, min(len(matrix), len(matrix[0]))):
            print('k', k)
            print(f'dir: {direction}. len(matrix)-k: {len(matrix)-k}')
            for _ in range(len(matrix) - k):
                pos = move(pos, direction)
                if pos:
                    res.append(matrix[pos[0]][pos[1]]) # 1
                    print(pos, matrix[pos[0]][pos[1]])
                else:
                    print('pos', pos)
            direction = changeDirection(direction)
            print(f'dir: {direction}. len(matrix[0])-k: {len(matrix[0])-k}')
            for _ in range(len(matrix[0]) - k):
                pos = move(pos, direction)
                if pos:
                    res.append(matrix[pos[0]][pos[1]]) # 2
                    print(pos, matrix[pos[0]][pos[1]])
                else:
                    print('pos', pos)
            direction = changeDirection(direction)

        if len(matrix) > len(matrix[0]):
            for _ in range(len(matrix) - len(matrix[0])):
                pos = move(pos, direction)
                res.append(matrix[pos[0]][pos[1]]) # 2
                print(pos, matrix[pos[0]][pos[1]])
                
        return res
        '''
        visited = [[True]*len(matrix[0])]
        for i in range(1, len(matrix)):
            visited.append([False]*len(matrix[0]))
        

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

        pos, direction = move(pos, direction, visited)
        while pos:
            res.append(matrix[pos[0]][pos[1]])
            pos, direction = move(pos, direction, visited)
        return res
        '''
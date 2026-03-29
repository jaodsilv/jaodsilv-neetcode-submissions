class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        if m == 1:
            return matrix[0]

        res = []
        if n == 1:
            for i in range(len(matrix)):
                res.append(matrix[i][0])
            return res
        i, j = 0, -1

        def moveRight(i, j, steps):
            if steps <= 0:
                return (i, j)
            for _ in range(steps):
                j += 1
                res.append(matrix[i][j])
            return (i, j)
        def moveLeft(i, j, steps):
            if steps <= 0:
                return (i, j)
            for _ in range(steps):
                j -= 1
                res.append(matrix[i][j])
            return (i, j)
        def moveDown(i, j, steps):
            if steps <= 0:
                return (i, j)
            for _ in range(steps):
                i += 1
                res.append(matrix[i][j])
            return (i, j)
        def moveUp(i, j, steps):
            if steps <= 0:
                return (i, j)
            for _ in range(steps):
                i -= 1
                res.append(matrix[i][j])
            return (i, j)
        
        # Initial Move
        i, j = moveRight(i, j, n)
        k = 1
        print(res)
        while m-k > 0:
            i, j = moveDown(i, j, m-k)
            print(res)
            if n-k <= 0:
                break
            i, j = moveLeft(i, j, n-k)
            print(res)
            k += 1
            if m-k <= 0:
                break
            i, j = moveUp(i, j, m-k)
            if n-k <= 0:
                break
            print(res)
            i, j = moveRight(i, j, n-k)
            print(res)
            k += 1
        return res


        '''
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]]

        [2,5],
        [8,4],
        [0,-1]
        '''


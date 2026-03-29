class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Let`s find the row first
        left = 0
        right = len(matrix)
        i = len(matrix) // 2
        print(i, right, left)
        while right - left > 1:
            # i != left: # or
            if matrix[i][0] == target:
                return True
            if matrix[i][0] < target:
                left = i
            else: # matrix[i][0] > target:
                right = i
            i = (right + left) // 2
            print(i, right, left)
        if i >= len(matrix):
            return False
        left = 0
        right = len(matrix[i])
        if right == 1:
            return matrix[i][0] == target
        j = len(matrix[i]) // 2
        print(i, j, right, left)
        while j != left or right - left > 1:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                left = j + 1
            else: # matrix[i][j] > target:
                right = j
            j = (right + left) // 2
            print(i, j, right, left)

        return j < len(matrix[i]) and matrix[i][j] == target
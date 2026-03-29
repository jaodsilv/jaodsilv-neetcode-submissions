class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    self._changeRowAndColumnTo0(matrix, i, j)
                elif matrix[i][j] is None:
                    matrix[i][j] = 0
    
    def _changeRowAndColumnTo0(self, matrix, i, j):
        for k in range(i):
            matrix[k][j] = 0
        for k in range(i+1, len(matrix)):
            if matrix[k][j] != 0:
                matrix[k][j] = None
        for k in range(j):
            matrix[i][k] = 0
        for k in range(j+1, len(matrix[i])):
            if matrix[i][k] != 0:
                matrix[i][k] = None
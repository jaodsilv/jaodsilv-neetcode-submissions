class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # We can, instead of doing every operation live, create a prefix sum matrix, one for vertical lists and nother for horizontal lists
        # Or perhaps a single one that has the sums from 0,0 to there
        self.prefixSum = []
        for i, r in enumerate(matrix):
            self.prefixSum.append([])
            for j, c in enumerate(r):
                self.prefixSum[-1].append(c + (self.prefixSum[i][j-1] if j > 0 else 0) + (self.prefixSum[i-1][j] if i > 0 else 0) - (self.prefixSum[i-1][j-1] if i > 0 and j > 0 else 0)) 


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # then, to calculate the rectangle we do?
        return self.prefixSum[row2][col2] - (self.prefixSum[row1-1][col2] if row1 > 0 else 0) - (self.prefixSum[row2][col1-1] if col1 > 0 else 0) + (self.prefixSum[row1-1][col1-1] if col1 > 0 and row1 > 0 else 0)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
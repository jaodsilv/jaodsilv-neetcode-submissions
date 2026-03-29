class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # We can think on deepness level
        l = len(matrix)
        for i in range(l // 2):
            for j in range(l // 2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[-j-1][i]
                matrix[-j-1][i] = matrix[-i-1][-j-1]
                matrix[-i-1][-j-1] = matrix[j][-i-1]
                matrix[j][-i-1] = tmp

        print(matrix)
        if l % 2 == 1:
            i = l // 2
            print (i)
            for j in range(l // 2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[-j-1][i]
                matrix[-j-1][i] = matrix[-i-1][-j-1]
                matrix[-i-1][-j-1] = matrix[j][-i-1]
                matrix[j][-i-1] = tmp

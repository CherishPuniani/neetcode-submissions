class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r = len(matrix)
        c = len(matrix[0])
        row = set()
        col = set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
            if i in row:
                matrix[i] = [0]*c
        
        for j in col:
            for i in range(r):
                matrix[i][j] = 0
        
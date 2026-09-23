class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r, c = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(c))
        first_col_zero = any(matrix[i][0] == 0 for i in range(r))

        # Use first row and column as markers
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero out cells based on markers
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out first row if needed
        if first_row_zero:
            for j in range(c):
                matrix[0][j] = 0

        # Zero out first column if needed
        if first_col_zero:
            for i in range(r):
                matrix[i][0] = 0
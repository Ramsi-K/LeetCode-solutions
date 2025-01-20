class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)  # Number of rows
        cols = len(grid[0])  # Number of columns

        # Step 1: Initialize row and column difference arrays
        row_differences = [0] * rows
        col_differences = [0] * cols

        # Step 2: Compute row and column differences
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    row_differences[i] += 1  # Increment for ones in the row
                    col_differences[j] += 1  # Increment for ones in the column
                else:
                    row_differences[i] -= 1  # Decrement for zeros in the row
                    col_differences[j] -= 1  # Decrement for zeros in the column

        # Step 3: Compute the final difference matrix
        for i in range(rows):
            for j in range(cols):
                grid[i][j] = row_differences[i] + col_differences[j]

        return grid
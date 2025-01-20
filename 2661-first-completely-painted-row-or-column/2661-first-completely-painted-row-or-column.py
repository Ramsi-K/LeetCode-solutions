class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])  # Dimensions of the matrix

        # Step 1: Create a mapping from numbers to their positions in the matrix
        num_to_position = {}
        for i in range(m):
            for j in range(n):
                num_to_position[mat[i][j]] = (i, j)

        # Step 2: Track painted rows and columns
        painted_rows = [0] * m  # Counts for rows
        painted_cols = [0] * n  # Counts for columns

        # Step 3: Simulate the painting process
        for idx, num in enumerate(arr):
            row, col = num_to_position[num]  # Get the row and column of the current number

            # Paint the row and column
            painted_rows[row] += 1
            painted_cols[col] += 1

            # Check if a row or column is fully painted
            if painted_rows[row] == n or painted_cols[col] == m:
                return idx  # Return the current index

        return -1  
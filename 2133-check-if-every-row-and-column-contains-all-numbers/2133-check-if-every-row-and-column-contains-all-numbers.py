class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        required_set = set(range(1, n + 1))  # The set {1, 2, ..., n}

        # Check rows and columns
        # Use zip to access columns
        for row, col in zip(matrix, zip(*matrix)):
            if set(row) != required_set or set(col) != required_set:
                return False

        return True

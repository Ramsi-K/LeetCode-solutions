class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        required_set = set(range(1, n + 1))  # The set {1, 2, ..., n}

        # Check rows and columns
        for i in range(n):
            # Validate row and column using set comprehension
            if set(matrix[i]) != required_set or set(matrix[j][i] for j in range(n)) != required_set:
                return False

        return True
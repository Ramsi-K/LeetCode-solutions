import numpy as np
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        
        # Convert binary string to array of integers
        binary_array = np.array([int(x) for x in boxes])
        
        # Create an n x n distance matrix
        indices = np.arange(n)
        distance_matrix = np.abs(indices[:, None] - indices)
        
        # Multiply distance matrix with binary array
        contribution_matrix = distance_matrix * binary_array
        
        # Sum rows to get the total operations for each box
        result = contribution_matrix.sum(axis=1)
        
        return result.tolist()


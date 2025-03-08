class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        min_ops = float('inf')  # Initialize with a large value
        
        # Iterate through all possible windows of size k
        for i in range(n - k + 1):
            # Count the number of 'W's in the current window
            ops = blocks[i:i + k].count('W')
            # Update the minimum operations
            if ops < min_ops:
                min_ops = ops
            # Early exit if the minimum possible is 0
            if min_ops == 0:
                break
        
        return min_ops
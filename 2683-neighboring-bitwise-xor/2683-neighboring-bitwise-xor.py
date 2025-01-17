class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)

        # Step 1: Check circularity by XORing all derived elements
        if sum(derived) % 2 != 0:
            return False
            
        # Helper function to check if a given starting value works
        def is_valid(start):
            original = [0] * n
            original[0] = start  # Set the first element
            for i in range(1, n):
                original[i] = original[i - 1] ^ derived[i - 1]  # Calculate the next value
            
            # Check the circular condition
            return (original[-1] ^ original[0]) == derived[-1]
        
        # Try both possible starting values for original[0]
        return is_valid(0) or is_valid(1)
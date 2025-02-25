class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        
        # Initialize counts
        odd_count = 0    # Number of prefix sums that are odd
        even_count = 1   # Number of prefix sums that are even (start with 1 for empty subarray)
        result = 0
        prefix_sum = 0
        
        for num in arr:
            # Update prefix sum
            prefix_sum += num
            
            # If current prefix sum is odd
            if prefix_sum % 2 == 1:
                # Add number of even prefix sums seen so far to result
                result = (result + even_count) % MOD
                # Increment odd count
                odd_count += 1
            else:
                # Add number of odd prefix sums seen so far to result
                result = (result + odd_count) % MOD
                # Increment even count
                even_count += 1
        
        return result

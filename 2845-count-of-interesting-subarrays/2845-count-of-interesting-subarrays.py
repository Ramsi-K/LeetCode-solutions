class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        # Transform the array into a binary array where 1 indicates nums[i] % modulo == k
        binary = [1 if x % modulo == k else 0 for x in nums]
        
        prefix_sum = 0
        count = 0
        # The hash map stores the frequency of each (prefix_sum % modulo)
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1  # initial prefix sum is 0
        
        for num in binary:
            prefix_sum += num
            key = (prefix_sum % modulo - k) % modulo
            count += prefix_counts.get(key, 0)
            # Update the current prefix_sum % modulo in the hash map
            current_mod = prefix_sum % modulo
            prefix_counts[current_mod] += 1
        
        return count
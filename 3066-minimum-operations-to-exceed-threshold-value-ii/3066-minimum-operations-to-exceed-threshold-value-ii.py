class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ops = 0
        
        while len(nums) >= 2 and nums[0] < k:
            # Remove the two smallest elements
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            # Combine them into a new number
            new_val = 2 * x + y
            # Add the new number back into the heap
            heapq.heappush(nums, new_val)
            ops += 1
        
        # If after all operations the smallest element is still less than k, it's impossible.
        return ops if nums and nums[0] >= k else -1
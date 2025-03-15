class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def can_rob(cap):
            """Check if we can rob at least k houses with max house value ≤ cap."""
            count, i = 0, 0
            while i < len(nums):
                if nums[i] <= cap:  # Can rob this house
                    count += 1
                    i += 1  # Skip next house to maintain non-adjacency
                i += 1  # Move to next house
            return count >= k  # Check if we robbed at least k houses

        low, high = min(nums), max(nums)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if can_rob(mid):  # If it's possible to rob at least k houses with cap=mid
                ans = mid  # Store as potential answer
                high = mid - 1  # Try to minimize further
            else:
                low = mid + 1  # Increase cap to allow more robberies

        return ans
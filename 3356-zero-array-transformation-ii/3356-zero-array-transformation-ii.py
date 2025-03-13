class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def can_zero_with_k(k):
            n = len(nums)
            arr = nums[:]  # Copy the original nums array
            diff = [0] * (n + 1)  # Difference array
    
            for i in range(k):
                l, r, val = queries[i]
                diff[l] -= val
                diff[r + 1] += val  # Apply range update

            # Apply prefix sum on difference array
            curr = 0
            for i in range(n):
                curr += diff[i]
                arr[i] += curr  # Apply accumulated decrement
                if arr[i] > 0:  # If any value is still > 0, we cannot zero it
                    return False

            return True

        # Edge Case: If nums is already all zeros, return 0 immediately
        if all(num == 0 for num in nums):
            return 0
        # Binary search for the minimum k
        low, high = 1, len(queries)
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if can_zero_with_k(mid):
                ans = mid
                high = mid - 1  # Try to minimize k
            else:
                low = mid + 1

        return ans
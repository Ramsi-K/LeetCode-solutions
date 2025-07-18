class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        left = [0] * (2 * n + 1)
        right = [0] * (2 * n + 1)

        # Left: min sum of n largest elements from first i elements
        max_heap = []
        total = 0
        for i in range(2 * n):
            heapq.heappush(max_heap, -nums[i])
            total += nums[i]
            if len(max_heap) > n:
                total += heapq.heappop(max_heap)  # remove largest 
            if len(max_heap) == n:
                left[i] = total

        # Right: max sum of n smallest elements from last i elements
        min_heap = []
        total = 0
        for i in range(3 * n - 1, n - 1, -1):
            heapq.heappush(min_heap, nums[i])
            total += nums[i]
            if len(min_heap) > n:
                total -= heapq.heappop(min_heap)  # remove smallest
            if len(min_heap) == n:
                right[i] = total

        # Compute minimum difference
        res = float('inf')
        for i in range(n - 1, 2 * n):
            res = min(res, left[i] - right[i + 1])

        return res

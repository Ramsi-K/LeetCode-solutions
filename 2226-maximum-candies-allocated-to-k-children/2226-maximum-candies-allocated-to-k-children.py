class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0  # Not enough candies for each child to get at least 1

        def can_allocate(c):
            return sum(candies[i] // c for i in range(len(candies))) >= k

        low, high = 1, max(candies)
        best = 0

        while low <= high:
            mid = (low + high) // 2
            if can_allocate(mid):
                best = mid  # Store the valid max `c`
                low = mid + 1  # Try to maximize further
            else:
                high = mid - 1  # Decrease `c`

        return best
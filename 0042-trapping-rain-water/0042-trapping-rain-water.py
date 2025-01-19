class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0  # Not enough bars to trap water

        # Step 1: Precompute left_max and right_max
        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        # Step 2: Calculate trapped water
        water = 0
        for i in range(n):
            water += max(0, min(left_max[i], right_max[i]) - height[i])

        return water
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0  # Not enough bars to trap water

        left, right = 0, n - 1
        left_max, right_max = 0, 0
        water = 0

        while left <= right:
            if left_max < right_max:
                # Process the left side
                if height[left] < left_max:
                    water += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                # Process the right side
                if height[right] < right_max:
                    water += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1

        return water
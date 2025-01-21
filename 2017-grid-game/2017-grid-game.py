class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        # Calculate prefix sums for both rows
        top_prefix = [0] * n
        bottom_prefix = [0] * n
        top_prefix[0] = grid[0][0]
        bottom_prefix[0] = grid[1][0]
        
        for i in range(1, n):
            top_prefix[i] = top_prefix[i - 1] + grid[0][i]
            bottom_prefix[i] = bottom_prefix[i - 1] + grid[1][i]
        
        # Minimum points the second robot can collect
        min_points = float('inf')
        
        for i in range(n):
            # Points left for the second robot if the first robot switches at column i
            points_top = top_prefix[-1] - top_prefix[i]  # Points above after column i
            points_bottom = bottom_prefix[i - 1] if i > 0 else 0  # Points below before column i
            
            # Max points the second robot can collect
            max_points_second_robot = max(points_top, points_bottom)
            min_points = min(min_points, max_points_second_robot)
        
        return min_points
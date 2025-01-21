class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])  # Number of columns
        remainingTopRow = sum(grid[0])  # Total points in the top row initially
        collectedBottomRow = 0  # Points collected in the bottom row so far
        maxPointsSecondRobot = []  # To store the maximum points the second robot can collect for each split

        for col in range(n):
            # Subtract the current cell from the remaining points in the top row
            remainingTopRow -= grid[0][col]
            
            # Calculate the maximum points the second robot can collect at this column
            maxPointsSecondRobot.append(max(remainingTopRow, collectedBottomRow))
            
            # Add the current cell to the collected points in the bottom row
            collectedBottomRow += grid[1][col]
        
        # The result is the minimum of the maximum points the second robot can collect
        return min(maxPointsSecondRobot)
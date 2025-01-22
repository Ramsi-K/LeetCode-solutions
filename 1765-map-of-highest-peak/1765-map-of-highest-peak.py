class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
    
        # Initialize the height matrix
        height = [[-1] * n for _ in range(m)]
        
        # Multi-source BFS queue initialized with all water cells
        queue = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0  # Water cells have height 0
                    queue.append((i, j))
        
        # Directions for adjacent cells (north, south, east, west)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Perform BFS
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Check if the neighbor is within bounds and unvisited
                if 0 <= nx < m and 0 <= ny < n and height[nx][ny] == -1:
                    height[nx][ny] = height[x][y] + 1  # Increment height
                    queue.append((nx, ny))
        
        return height
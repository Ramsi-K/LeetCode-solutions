class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        deque_queue = deque()  # Deque for BFS-like traversal

        # Add all boundary cells to the deque
        for i in range(m):
            for j in [0, n - 1]:  # Left and right boundaries
                deque_queue.append((heightMap[i][j], i, j))
                visited[i][j] = True
        for j in range(n):
            for i in [0, m - 1]:  # Top and bottom boundaries
                deque_queue.append((heightMap[i][j], i, j))
                visited[i][j] = True

        water_trapped = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, left, down, up

        # Process cells
        while deque_queue:
            height, x, y = deque_queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    # Calculate trapped water
                    trapped = max(0, height - heightMap[nx][ny])
                    water_trapped += trapped
                    
                    # Update the neighbor's height to the boundary height
                    new_height = max(height, heightMap[nx][ny])
                    deque_queue.append((new_height, nx, ny))
                    visited[nx][ny] = True

        return water_trapped
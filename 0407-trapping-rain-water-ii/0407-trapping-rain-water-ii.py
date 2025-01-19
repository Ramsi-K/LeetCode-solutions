class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []

        # Step 1: Add all boundary cells to the heap
        for i in range(m):
            for j in [0, n - 1]:  # Left and right boundaries
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        for j in range(n):
            for i in [0, m - 1]:  # Top and bottom boundaries
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True

        # Step 2: Process the heap
        water_trapped = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, left, down, up

        while heap:
            height, x, y = heapq.heappop(heap)
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    # Calculate trapped water
                    water_trapped += max(0, height - heightMap[nx][ny])
                    # Update the height of the neighbor
                    heapq.heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))
                    visited[nx][ny] = True

        return water_trapped
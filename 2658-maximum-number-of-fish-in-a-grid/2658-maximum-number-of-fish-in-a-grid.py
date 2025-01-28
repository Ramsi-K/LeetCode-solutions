from collections import deque

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        max_fish = 0
        visited = [[False] * n for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    queue = deque([(i, j)])
                    visited[i][j] = True
                    current_sum = 0
                    while queue:
                        x, y = queue.popleft()
                        current_sum += grid[x][y]
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] > 0:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                    max_fish = max(max_fish, current_sum)
        
        return max_fish
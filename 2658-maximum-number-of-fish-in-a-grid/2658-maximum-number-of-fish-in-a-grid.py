from collections import deque

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0
        max_fish = 0
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    # BFS to find all connected cells
                    queue = deque()
                    queue.append((i, j))
                    visited[i][j] = True
                    current_sum = grid[i][j]
                    max_fish = max(max_fish, current_sum)
                    
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx = x + dx
                            ny = y + dy
                            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] > 0:
                                visited[nx][ny] = True
                                current_sum += grid[nx][ny]
                                queue.append((nx, ny))
                                max_fish = max(max_fish, current_sum)
        
        return max_fish
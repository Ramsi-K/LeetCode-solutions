class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        
        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))
            servers = [(r, c)]
            
            while queue:
                x, y = queue.popleft()
                for i in range(rows):
                    if grid[i][y] == 1 and (i, y) not in visited:
                        visited.add((i, y))
                        queue.append((i, y))
                        servers.append((i, y))
                for j in range(cols):
                    if grid[x][j] == 1 and (x, j) not in visited:
                        visited.add((x, j))
                        queue.append((x, j))
                        servers.append((x, j))
            
            if len(servers) > 1:
                return len(servers)
            return 0
        
        total_servers = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    total_servers += bfs(i, j)
        
        return total_servers


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_id = 2  # Start from 2 since 0 and 1 are already in the grid
        island_sizes = {0: 0}  # Default size for water
        
        # Helper function for DFS traversal
        def dfs(r, c, island_id):
            stack = [(r, c)]
            size = 0
            while stack:
                x, y = stack.pop()
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = island_id
                    size += 1
                    stack.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])
            return size
        
        # Step 1: Find all islands and their sizes
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_sizes[island_id] = dfs(r, c, island_id)
                    island_id += 1
        
        # Step 2: Try flipping each zero and compute possible max island size
        max_island = max(island_sizes.values())  # At least one island exists
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    new_size = 1  # Flipping this zero
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            seen.add(grid[nr][nc])  # Unique island IDs
                    new_size += sum(island_sizes[i] for i in seen)
                    max_island = max(max_island, new_size)
        
        return max_island
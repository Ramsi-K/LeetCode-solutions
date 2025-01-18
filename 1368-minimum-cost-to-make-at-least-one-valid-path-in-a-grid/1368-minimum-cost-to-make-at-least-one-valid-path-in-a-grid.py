class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
        costs = [[float('inf')] * n for _ in range(m)]
        queue = deque([(0, 0, 0)])  # (i, j, cost)
        costs[0][0] = 0

        while queue:
            i, j, cost = queue.popleft()
            
            # If we reached the end, return the cost
            if (i, j) == (m-1, n-1):
                return cost
            
            for idx, (di, dj) in enumerate(directions):
                ni, nj = i + di, j + dj
                
                if 0 <= ni < m and 0 <= nj < n:
                    # Determine if modification is needed
                    new_cost = cost + (1 if grid[i][j] != idx + 1 else 0)
                    
                    if new_cost < costs[ni][nj]:
                        costs[ni][nj] = new_cost
                        if grid[i][j] == idx + 1:
                            queue.appendleft((ni, nj, new_cost))  # Priority for no-cost moves
                        else:
                            queue.append((ni, nj, new_cost)) 
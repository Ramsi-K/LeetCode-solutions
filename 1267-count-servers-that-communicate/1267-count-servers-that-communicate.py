class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        row_sum = [sum(grid[i]) for i in range(rows)]
        col_sum = [sum(grid[i][j] for i in range(rows)) for j in range(cols)]
        
        communicating_servers = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (row_sum[i] > 1 or col_sum[j] > 1):
                    communicating_servers += 1
        
        return communicating_servers
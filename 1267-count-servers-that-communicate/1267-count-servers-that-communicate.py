class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        row_count = [0] * rows
        col_count = [0] * cols
        
        # Count servers in each row and column
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        
        # Count servers that can communicate
        communicating_servers = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    communicating_servers += 1
        
        return communicating_servers
        # rows = len(grid)
        # cols = len(grid[0])
        
        # row_sum = [sum(grid[i]) for i in range(rows)]
        # col_sum = [sum(grid[i][j] for i in range(rows)) for j in range(cols)]
        
        # communicating_servers = 0
        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == 1 and (row_sum[i] > 1 or col_sum[j] > 1):
        #             communicating_servers += 1
        
        # return communicating_servers
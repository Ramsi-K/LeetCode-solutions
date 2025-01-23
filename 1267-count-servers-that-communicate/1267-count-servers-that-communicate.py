class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        num_rows = len(grid) 
        total_communicating_servers = 0 

        for row_index in range(num_rows):
            row_sum = sum(grid[row_index]) 

            # If more than one server is present in the row, they can communicate
            if row_sum > 1:
                total_communicating_servers += row_sum
                continue

            # If there is exactly one server in the row, check the column
            elif row_sum == 1:
                column_sum = 0  
                column_index = grid[row_index].index(1) 

                # Sum the servers in the current column
                for row in range(num_rows):
                    column_sum += grid[row][column_index]

                    if column_sum > 1:
                        total_communicating_servers += 1
                        break

        return total_communicating_servers

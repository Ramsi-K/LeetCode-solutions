class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        empty_cells = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty_cells.append((i, j))
        if len(empty_cells) == 0:
            return
        
        self.find_solution = False
        
        def get_valid_numbers(row, col):
            valid = set('123456789')
            for j in range(9):
                valid.discard(board[row][j])
            for i in range(9):
                valid.discard(board[i][col])
            r = row // 3 * 3
            c = col // 3 * 3
            for i in range(3):
                for j in range(3):
                    valid.discard(board[r + i][c + j])
            return valid
        
        def backtrack(index=0):
            if index == len(empty_cells):
                self.find_solution = True
            if self.find_solution:
                return
            row, col = empty_cells[index]
            valid_numbers = get_valid_numbers(row, col)
            for number in valid_numbers:
                if not self.find_solution:
                    board[row][col] = number
                    backtrack(index + 1)
                    if not self.find_solution:
                        board[row][col] = '.'
        
        backtrack()
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def f(r, c):
            o = [0, 1, 2, 5, 8, 7, 6, 3]
            s = ""
            for k in o:
                s += str(grid[r + k // 3][c + k % 3])
            return grid[r][c] % 2 == 0 and (
                s in "43816729" * 2 or s in "43816729"[::-1] * 2
            )

        n = len(grid)
        m = len(grid[0])
        a = 0
        for i in range(n - 2):
            for j in range(m - 2):
                if grid[i + 1][j + 1] == 5 and f(i, j):
                    a += 1
        return a

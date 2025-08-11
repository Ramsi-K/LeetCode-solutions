MOD = 10**9 + 7
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        while n:
            low_bit = n & -n
            powers.append(low_bit)
            n ^= low_bit

        size = len(powers)
        table = [[0]*size for _ in range(size)]
        for row, val in enumerate(powers):
            table[row][row] = val
            for col in range(row+1, size):
                table[row][col] = (table[row][col-1] * powers[col] % MOD)

        return [table[p][q] for p, q in queries]
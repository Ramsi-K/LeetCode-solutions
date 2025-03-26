class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat = [num for row in grid for num in row]
        mod = flat[0] % x
        for num in flat:
            if num % x != mod:
                return -1

        flat.sort()
        median = flat[len(flat) // 2]
        return sum(abs(num - median) // x for num in flat)
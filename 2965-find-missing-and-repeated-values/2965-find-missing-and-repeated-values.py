class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_numbers = n * n
        freq = [0] * (total_numbers + 1)  # Frequency array
        
        # Flatten the grid and count frequencies
        for row in grid:
            for num in row:
                freq[num] += 1
        
        a, b = -1, -1
        for num in range(1, total_numbers + 1):
            if freq[num] == 2:
                a = num
            elif freq[num] == 0:
                b = num
        
        return [a, b]
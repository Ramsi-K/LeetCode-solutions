class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = Counter(tiles)
        self.count = 0
        
        def dfs():
            for tile in list(freq.keys()):
                if freq[tile] > 0:
                    self.count += 1  # Count this sequence (each new addition makes a new sequence)
                    freq[tile] -= 1
                    dfs()
                    freq[tile] += 1  # Backtrack
        
        dfs()
        return self.count
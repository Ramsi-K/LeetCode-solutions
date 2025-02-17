class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = Counter(tiles)
        letters = list(freq.keys())
        n = len(letters)
        
        # Recursive helper function that iterates over distinct letters.
        # current is a list of counts chosen for letters[0...i-1].
        def helper(i, current):
            if i == n:
                total = sum(current)
                # Exclude the empty selection.
                if total == 0:
                    return 0
                # Compute multinomial: total! / (current[0]! * current[1]! * ... * current[n-1]!)
                ways = factorial(total)
                for c in current:
                    ways //= factorial(c)
                return ways
            result = 0
            # For the current letter, choose any count from 0 up to its frequency.
            for count in range(freq[letters[i]] + 1):
                current.append(count)
                result += helper(i + 1, current)
                current.pop()
            return result
        
        return helper(0, [])

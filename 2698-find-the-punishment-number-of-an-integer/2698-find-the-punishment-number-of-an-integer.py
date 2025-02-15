class Solution:
    def punishmentNumber(self, n: int) -> int:
        # Helper function that checks if we can partition the string s
        # into contiguous substrings whose sum equals target.
        def canPartition(s: str, target: int) -> bool:
            L = len(s)
            
            # DFS function: starting at index `i`, with current sum `cur`
            def dfs(i: int, cur: int) -> bool:
                # If we've reached the end, check if we hit the target sum.
                if i == L:
                    return cur == target
                # Try all possible splits starting from index i.
                for j in range(i + 1, L + 1):
                    # Convert the substring s[i:j] to an integer.
                    part = int(s[i:j])
                    # If we can complete a valid partition from j onward, return True.
                    if dfs(j, cur + part):
                        return True
                return False
            
            return dfs(0, 0)
        
        punishment = 0
        # Check each integer i in [1, n]
        for i in range(1, n + 1):
            square = i * i
            s = str(square)
            if canPartition(s, i):
                punishment += square
        return punishment


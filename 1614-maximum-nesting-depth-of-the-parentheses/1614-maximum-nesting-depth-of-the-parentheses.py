class Solution:
    def maxDepth(self, s: str) -> int:
        curr_depth = max_depth = 0

        for char in s:
            if char == "(": 
                curr_depth += 1
                max_depth = max(curr_depth, max_depth)
            elif char == ")":
                curr_depth -= 1

        
        return max_depth


class Solution:
    def maxDepth(self, s: str) -> int:
        curr_depth = max_depth = 0

        for char in s:
            if char == "(": 
                curr_depth += 1
            elif char == ")":
                curr_depth -= 1
            
            if curr_depth > max_depth:
                max_depth = curr_depth
        
        return max_depth


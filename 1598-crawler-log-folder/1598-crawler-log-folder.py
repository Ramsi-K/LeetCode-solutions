class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for action in logs:
            if depth > 0 and action == "../":
                depth -= 1
            elif action == "./" or action == "../":
                continue
            else:
                depth += 1
        
        return depth


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        target_indices = [i for i, x in enumerate(s) if x == c]
        # return [min(abs(i - j) for j in target_indices) for i in range(len(s))]
        # Initialize result array with a high number
        result = [float('inf')] * len(s)
        
        # Iterate through the string and find minimum distances
        closest = float('inf')
        for i in range(len(s)):
            if s[i] == c:
                closest = i
            result[i] = abs(i - closest)
        
        # Iterate backwards to handle cases where 'c' appears after the current index
        closest = float('inf')
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                closest = i
            result[i] = min(result[i], abs(i - closest))
        
        return result
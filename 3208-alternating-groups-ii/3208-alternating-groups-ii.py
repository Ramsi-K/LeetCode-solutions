class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        count = 0
        left = 0

        # Iterate through the extended array (n + k - 1)
        for right in range(n + k - 1):
            # If alternation breaks, move the left pointer
            if right > 0 and colors[right % n] == colors[(right - 1) % n]:
                left = right
            
            # If the window size is at least k, increment the count
            if right - left + 1 >= k:
                count += 1
        
        return count
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        result = [1, 0]

        for char in s:
            width = widths[ord(char) - ord('a')]
            if result[1] + width > 100:
                result[0] += 1 
                result[1] = width 
            else:
                result[1] += width  

        return result
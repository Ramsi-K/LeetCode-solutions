class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        result = [1, 0]
        letter_to_width = {letter: widths[i] for i, letter in enumerate(string.ascii_lowercase)}

        for char in s:
            width = letter_to_width[char]
            if result[1] + width > 100:
                result[0] += 1 
                result[1] = width 
            else:
                result[1] += width  

        return result
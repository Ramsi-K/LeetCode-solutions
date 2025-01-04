class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        unique_palindromes = set()
        
        for char in set(s):
            # Find all positions of the character in the string
            first = s.find(char)
            last = s.rfind(char)
            
            # If there's space for a middle character
            if last - first > 1:
                for mid_char in set(s[first + 1 : last]):
                    unique_palindromes.add(char + mid_char + char)
        
        return len(unique_palindromes)
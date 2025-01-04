class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        unique_palindromes = set()
            
        for char in set(s):
            first = s.find(char)
            last = s.rfind(char)
            
            if last - first > 1:
                # Create a bitmask for intermediate characters
                bitmask = 0
                for mid_char in s[first + 1 : last]:
                    bitmask |= (1 << (ord(mid_char) - ord('a')))
                
                # Check all possible middle characters
                for i in range(26):
                    if bitmask & (1 << i):
                        unique_palindromes.add(char + chr(i + ord('a')) + char)
        
        return len(unique_palindromes)
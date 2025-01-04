class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:     
        left = Counter()
        right = Counter(s)
        unique_palindromes = set()
        
        for i, char in enumerate(s):
            right[char] -= 1
            if right[char] == 0:
                del right[char]
            
            # Check for palindromes
            for c in left:
                if c in right:
                    unique_palindromes.add(c + char + c)
            
            left[char] += 1
        
        return len(unique_palindromes)
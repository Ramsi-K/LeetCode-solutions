class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        prefix = [[0] * 26 for _ in range(n)]
        
        # Build prefix sum
        for i in range(n):
            if i > 0:
                prefix[i] = prefix[i - 1][:]
            prefix[i][ord(s[i]) - ord('a')] += 1
        
        unique_palindromes = set()
        
        # Iterate over each middle character
        for i, char in enumerate(s):
            left = prefix[i - 1] if i > 0 else [0] * 26
            right = [prefix[n - 1][j] - prefix[i][j] for j in range(26)]
            
            for c in range(26):
                if left[c] > 0 and right[c] > 0:
                    unique_palindromes.add(chr(c + ord('a')) + char + chr(c + ord('a')))
        
        return len(unique_palindromes)
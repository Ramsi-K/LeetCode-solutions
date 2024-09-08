class Solution:
    def longestPalindrome(self, s: str) -> int:
        mapping = {s[i]: s.count(s[i]) for i in range(len(s))}
        # print(mapping)

        len_of_palindrome = 0
        center = None
        for k, v in mapping.items():
            # print(k, v)
            if v == 1: 
                center = k
                
            elif v % 2 == 0: 
                len_of_palindrome += v
            
            elif v > 2: 
                len_of_palindrome += 2 * (v // 2)
                center = k
        
        if center: len_of_palindrome += 1
        # print(len_of_palindrome)
        return len_of_palindrome

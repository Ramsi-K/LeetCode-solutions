class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def is_vowel(ch: str) -> bool:
            return ch in {'a', 'e', 'i', 'o', 'u'}
    
        # Step 1: Build the prefix sum array
        n = len(words)
        prefix = [0] * n
        prefix[0] = 1 if is_vowel(words[0][0]) and is_vowel(words[0][-1]) else 0
        
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + (1 if is_vowel(words[i][0]) and is_vowel(words[i][-1]) else 0)
        
        # Step 2: Answer each query
        ans = []
        for l, r in queries:
            if l == 0:
                ans.append(prefix[r])
            else:
                ans.append(prefix[r] - prefix[l - 1])
        
        return ans
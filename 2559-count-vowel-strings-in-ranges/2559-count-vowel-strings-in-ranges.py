class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def is_vowel(ch: str) -> bool:
            return ch in {'a', 'e', 'i', 'o', 'u'}
    
        # Step 1: Create the binary array
        binary = [
            1 if is_vowel(word[0]) and is_vowel(word[-1]) else 0
            for word in words
        ]
        
        # Step 2: Build the prefix sum array
        prefix = [0] * len(binary)
        prefix[0] = binary[0]
        for i in range(1, len(binary)):
            prefix[i] = prefix[i - 1] + binary[i]
        
        # Step 3: Answer each query
        ans = []
        for l, r in queries:
            if l == 0:
                ans.append(prefix[r])
            else:
                ans.append(prefix[r] - prefix[l - 1])
        
        return ans
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = 0
        for i, char in enumerate(word):
            if char == ch:
                n = i+1
                break

        return word[:n][::-1] + word[n:]
        

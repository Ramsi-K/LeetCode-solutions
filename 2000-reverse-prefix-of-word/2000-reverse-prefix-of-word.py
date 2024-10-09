class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = 0
        for i in range(len(word)):
            if word[i] == ch:
                n = i+1
                break

        return word[:n][::-1] + word[n:]
        

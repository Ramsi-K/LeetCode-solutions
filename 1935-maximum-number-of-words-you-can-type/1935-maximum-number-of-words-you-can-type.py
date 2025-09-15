class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters) 
        words = text.split()
        count = 0
        for word in words:
            if not (set(word) & broken):  
                count += 1
        return count
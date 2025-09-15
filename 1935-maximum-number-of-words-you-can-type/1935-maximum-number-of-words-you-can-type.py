class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        letters = list(brokenLetters)
        count = len(words)
        for word in words:
            if any(letter in letters for letter in word):
                count -= 1
        
        return count
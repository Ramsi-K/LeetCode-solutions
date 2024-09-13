class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word == word.upper() or word == word.lower() or word == word.capitalize()
        # return word in [word.upper(), word.lower(), word.capitalize()]
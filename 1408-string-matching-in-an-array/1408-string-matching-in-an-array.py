class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        superstring = " ".join(words)
        return [word for word in words if superstring.count(word) > 1]
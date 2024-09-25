class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = Counter(s1.split() + s2.split())
        return [k for k, c in words.items() if c == 1]

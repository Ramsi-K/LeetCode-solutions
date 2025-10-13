class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]
        n = len(words)
        lower = Counter(words[0])

        for i in range(1, n):
            if not lower == Counter(words[i]):
                lower = Counter(words[i])
                res.append(words[i])

        return res
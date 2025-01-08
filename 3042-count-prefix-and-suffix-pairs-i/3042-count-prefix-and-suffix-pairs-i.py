class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            # Check if str1 is both a prefix and a suffix of str2
            return str2.startswith(str1) and str2.endswith(str1)

        n = len(words)
        count = 0

        # Iterate through all pairs (i, j) with i < j
        for i in range(n):
            for j in range(i + 1, n):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1

        return count
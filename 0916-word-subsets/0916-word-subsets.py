class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def countFrequency(word):
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            return freq

        # Step 1: Merge requirements from words2
        max_requirements = [0] * 26
        for word in words2:
            word_freq = countFrequency(word)
            for i in range(26):
                max_requirements[i] = max(max_requirements[i], word_freq[i])

        # Step 2: Check each word in words1 against max_requirements
        result = []
        for word in words1:
            word_freq = countFrequency(word)
            if all(word_freq[i] >= max_requirements[i] for i in range(26)):
                result.append(word)

        return result
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        combined_count = Counter()
        for b in words2:
            b_count = Counter(b)
            for char in b_count:
                combined_count[char] = max(combined_count[char], b_count[char])

        # Check each word in words1 against the combined requirement
        result = []
        for word in words1:
            a_count = Counter(word)
            if all(a_count[char] >= combined_count[char] for char in combined_count):
                result.append(word)

        return result
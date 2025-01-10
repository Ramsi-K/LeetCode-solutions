class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def isSubset(a_count, b_count):
            for char in b_count:
                if b_count[char] > a_count.get(char, 0):
                    return False
            return True

        result = []
        b_counts = [Counter(b) for b in words2]

        for word in words1:
            a_count = Counter(word)
            if all(isSubset(a_count, b_count) for b_count in b_counts):
                result.append(word)

        return result
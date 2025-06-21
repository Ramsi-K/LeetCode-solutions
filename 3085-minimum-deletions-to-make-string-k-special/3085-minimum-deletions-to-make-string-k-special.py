import collections

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counts = sorted(collections.Counter(word).values())

        def get_min_deletions(i):
            if i == len(counts):
                return float('inf')
            smallest = counts[i]

            result = 0
            for j in reversed(range(i + 1, len(counts))):
                delta = counts[j] - (smallest + k)
                if delta <= 0:
                    break
                result += delta
            return min(result, smallest + get_min_deletions(i + 1))

        return get_min_deletions(0)
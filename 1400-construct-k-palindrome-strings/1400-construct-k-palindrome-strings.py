class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # If there are fewer characters than k, it's impossible
        if len(s) < k:
            return False

        # Count the frequency of each character
        char_count = Counter(s)

        # Count characters with odd frequencies
        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)

        # Check if the odd counts fit within k
        return odd_count <= k
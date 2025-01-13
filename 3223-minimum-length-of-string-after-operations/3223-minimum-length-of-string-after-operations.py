class Solution:
    def minimumLength(self, s: str) -> int:
        char_count = Counter(s)
        ans = 0

        # Iterate through each character's count
        for count in char_count.values():
            if count & 1:  # Odd count
                ans += 1
            elif count != 0:  # Even count
                ans += 2

        return ans
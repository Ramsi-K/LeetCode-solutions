class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = Counter(s)
        return next((i for i, char in enumerate(s) if char_count[char] == 1), -1)
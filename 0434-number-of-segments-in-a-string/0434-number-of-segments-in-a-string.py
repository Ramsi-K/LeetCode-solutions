class Solution:
    def countSegments(self, s: str) -> int:
        return len([x for x in s.strip().split(" ") if x])
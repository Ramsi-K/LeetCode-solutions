class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = list(map(int, str(int("".join(map(str, digits))) + 1)))
        return num
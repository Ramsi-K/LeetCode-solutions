class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)

        for i, n in enumerate(sorted(capacity, reverse=True)):
            total -= n
            if total <= 0:
                return i + 1

        return -1

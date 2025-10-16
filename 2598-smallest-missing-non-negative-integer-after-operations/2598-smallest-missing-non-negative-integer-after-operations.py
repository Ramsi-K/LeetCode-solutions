class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # I still don't understand this question
        # the best i got is group numbers by remainder and count how far you can go
        freq = [0] * value
        for a in nums:
            r = a % value
            if r < 0:
                r += value
            freq[r] += 1

        x = 0
        while True:
            r = x % value
            if freq[r] == 0:
                return x
            freq[r] -= 1
            x += 1
        
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        remainder = total % 3
        if remainder == 0:
            return total

        ones = [num for num in nums if num % 3 == 1]
        twos = [num for num in nums if num % 3 == 2]

        ones.sort()
        twos.sort()

        # candidates after subtracting the minimal thing(s)
        candidates = []

        if remainder == 1:
            # remove one smallest remainder-1
            if ones:
                candidates.append(total - ones[0])
            # or remove two smallest remainder-2
            if len(twos) >= 2:
                candidates.append(total - twos[0] - twos[1])
        else:  # r == 2
            # remove one smallest remainder-2
            if twos:
                candidates.append(total - twos[0])
            # or remove two smallest remainder-1
            if len(ones) >= 2:
                candidates.append(total - ones[0] - ones[1])

        return max(candidates) if candidates else 0

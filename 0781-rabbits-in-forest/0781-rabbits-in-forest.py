class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        res = 0
        for x, freq in count.items():
            group_size = x + 1
            groups = math.ceil(freq / group_size)
            res += groups * group_size
        return res
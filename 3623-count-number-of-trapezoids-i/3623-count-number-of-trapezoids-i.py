class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = 10**9 + 7
        groups = defaultdict(int)
        for x, y in points:
            groups[y] += 1
        a = []
        for count in groups.values():
            if count >= 2:
                a.append(count * (count - 1) // 2)
        S = sum(a)
        T = sum(x * x for x in a)
        return (S * S - T) // 2 % mod

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        l = []
        n = len(colors)
        for i in range(n - 1):
            if colors[i] == colors[i + 1]:
                l.append(i)

        if colors[n - 1] == colors[0]:
            l.append(n - 1)
        if len(l) == 0:
            return n

        l.append(l[0] + n)
        res = 0
        for i in range(len(l) - 1):
            res += max(0, l[i + 1] - l[i] - k + 1)

        return res
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        out = [x for x in t if t.count(x) > s.count(x)]
        # print(out)
        return out[0]
        
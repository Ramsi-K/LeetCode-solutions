class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s): return False
        out = []
        for i in s:
            # print(i)
            ind = t.find(i)
            out.append(ind)
            t = t.replace(t[:ind+1], "%"*(ind+1), 1)
            # print(t)
        
        # if any(x == -1 for x in out): return False
        # print(out)
        # print(out == sorted(out))
        return (out == sorted(out))

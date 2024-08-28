class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)): return False

        map_s = {s[i]: t[i] for i in range(len(s))}
        
        for i in range(len(t)):
            if t[i] != map_s[s[i]]:
                return False

        return True
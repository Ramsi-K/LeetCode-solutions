class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or len(set(s)) != len(set(t)): return False
        
        a = len(s)
        map_s = {s[i]: s.count(s[i]) for i in range(a)}
        map_t = {t[i]: t.count(t[i]) for i in range(a)}
        # print(map_s, map_t, map_s == map_t)

        return map_s == map_t
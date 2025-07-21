class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s)<=2: return s
        res = [s[0], s[1]]

        for char in s[2:]:
            print(char)
            if res[-1] == res[-2] == char: continue
            res.append(char)

        return "".join(res)

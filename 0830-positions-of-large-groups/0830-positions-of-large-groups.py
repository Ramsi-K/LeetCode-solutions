class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        out = []
        i = 0
        if len(s) <= 2: return []

        while i < len(s)-2:
            if s[i] == s[i+1] == s[i+2]:
                start = i
                end = i+2
                while end + 1 < len(s) and s[end + 1] == s[i]:
                    end += 1
                out.append([start, end])
                i = end + 1
            else:
                i+=1
        # print(out)
        return out








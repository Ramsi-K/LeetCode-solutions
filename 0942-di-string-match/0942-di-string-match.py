class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        low, high = 0, n
        perm = []

        for char in s:
            # print(char)
            if char == "I": 
                perm.append(low)
                low += 1
            else:
                perm.append(high)
                high -= 1
            
        perm.append(low)
        # print(perm)
        return perm
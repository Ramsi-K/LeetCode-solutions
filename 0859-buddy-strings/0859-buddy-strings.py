class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        if s == goal: return len(set(s)) < len(s)
        mismatch = [(a,b) for a,b in zip(s, goal) if a != b]
        # print(mismatch)
        if len(mismatch) == 2 and mismatch[0] == mismatch[1][::-1]:
            return True
        
        return False


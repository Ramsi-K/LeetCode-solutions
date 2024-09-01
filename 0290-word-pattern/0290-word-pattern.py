class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list(pattern)
        s = s.split()

        if len(set(pattern)) != len(set(s)): return False

        translate_dict  = {pattern[i]: s[i] for i in range(len(pattern))}
        trans = str.maketrans(translate_dict)
        pattern_after = [s.translate(trans) for s in pattern]

        return pattern_after == s
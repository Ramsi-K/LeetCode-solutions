class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote) : return False

        for r in ransomNote:
            if r not in magazine: return False
            else: magazine = magazine.replace(r, '', 1)


        # print([r in magazine for r in ransomNote])
        return True
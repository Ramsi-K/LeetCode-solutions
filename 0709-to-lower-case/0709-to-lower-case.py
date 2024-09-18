class Solution:
    def toLowerCase(self, s: str) -> str:
        out = ""

        for char in s:
            if char.isupper(): out += char.lower()
            else: out += char

        return out
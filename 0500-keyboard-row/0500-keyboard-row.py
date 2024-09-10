class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        my_dict = {"row1" : "qwertyuiop", "row2": "asdfghjkl", "row3": "zxcvbnm"}
        new_dict = {i: v for i in words for v in my_dict.values() if i[0].lower() in v}

        out = [word for word in words if any(all(char in v for char in word.lower()) for v in my_dict.values())]

        return out


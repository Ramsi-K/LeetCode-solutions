class Solution:
    def isPalindrome(self, s: str) -> bool:
        translator = str.maketrans("", "", string.punctuation + string.whitespace)
        text = s.translate(translator).lower()
        pointer_1 = 0
        pointer_2 = len(text)-1
        print(text)
        while pointer_1 < pointer_2:
            print(f"Pointer_1: {text[pointer_1]}, Pointer_2: {text[pointer_2]}")
            if text[pointer_1] == text[pointer_2]: 
                pointer_1 += 1
                pointer_2 -= 1
                continue
            else: return False
        return True
        
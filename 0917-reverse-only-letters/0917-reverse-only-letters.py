class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [char for char in s if char.isalpha()]  # Step 1: Extract letters
        letters.reverse()  # Step 2: Reverse the letters
        
        out = ""
        letter_index = 0  
        for char in s:
            if char.isalpha():
                out += letters[letter_index]  # Add from the reversed list
                letter_index += 1
            else:
                out += char  # Keep non-letter characters unchanged
        # print(out)
        return out
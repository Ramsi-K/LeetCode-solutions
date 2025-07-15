class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False
        
        word = word.lower()
        vowels = "aeiou"
        vowel_counter = 0
        consonant_counter = 0
        
        for char in word:
            if not char.isdigit() and not char.isalpha(): 
                # print("not valid", char)
                return False
                break        
            elif char.isalpha():
                if char in vowels:
                    vowel_counter += 1
                else:
                    consonant_counter += 1

            
        return vowel_counter>0 and consonant_counter>0
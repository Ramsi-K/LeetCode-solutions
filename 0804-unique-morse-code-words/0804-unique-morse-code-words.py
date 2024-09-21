class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        letter_to_morse = {chr(i + ord('a')): morse_code[i] for i in range(26)}
        
        unique_transformations = {"".join(letter_to_morse[char] for char in word) for word in words}
        
        return len(unique_transformations)

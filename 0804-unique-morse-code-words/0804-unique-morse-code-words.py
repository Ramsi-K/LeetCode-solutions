class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        letter_to_morse = {letter: morse_code[i] for i, letter in enumerate(string.ascii_lowercase)}
        
        unique_transformations = {"".join(letter_to_morse[char] for char in word) for word in words}
        
        return len(unique_transformations)

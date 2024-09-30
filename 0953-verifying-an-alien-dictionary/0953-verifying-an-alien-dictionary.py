class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_map = {char: i  for i, char in enumerate(order)}

        def is_lexico(word1, word2):
            for c1, c2 in zip(word1, word2):
                if alien_map[c1] < alien_map[c2]:
                    return True 
                elif alien_map[c1] > alien_map[c2]:
                    return False  
            return len(word1) <= len(word2)

        for i in range(len(words) - 1):
                if not is_lexico(words[i], words[i + 1]):
                    return False
    
        return True
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lp_counts = Counter(char.lower() for char in licensePlate if char.isalpha())        
        shortest_word = None

        for word in words:
            word_counts = Counter(word)
            
            if all(word_counts[char] >= lp_counts[char] for char in lp_counts):
                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word = word

        return shortest_word

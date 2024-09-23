class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Remove punctuation and convert to lowercase
        paragraph = re.sub(r'[^\w\s]', ' ', paragraph.lower())
        
        # Split the paragraph by space and commas
        words = paragraph.split()
        
        # Filter out banned words
        words = [word for word in words if word not in banned]
        
        # Count word occurrences
        word_count = Counter(words)
        
        # Return the word with the highest frequency
        return word_count.most_common(1)[0][0]
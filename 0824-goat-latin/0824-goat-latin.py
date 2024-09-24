class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = "aeiouAEIOU"
        words = sentence.split(" ")

        suffixes = ["ma" + "a" * (i + 1) for i in range(len(words))]  # Precompute suffixes
        result = []
        
        for i in range(len(words)):
            word = words[i]
            if word[0] in vowels:
                result.append(f"{word}{suffixes[i]}")
            else:
                result.append(f"{word[1:]}{word[0]}{suffixes[i]}")

        return " ".join(result)
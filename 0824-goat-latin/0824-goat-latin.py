class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = "aeiouAEIOU"
        words = sentence.split(" ")

        suffixes = ["ma" + "a" * (i + 1) for i in range(len(words))]  # Precompute suffixes

        result = [
            f"{word}{suffixes[i]}" if word[0] in vowels else f"{word[1:]}{word[0]}{suffixes[i]}"
            for i, word in enumerate(words)
        ]

        return " ".join(result)
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(" ")

        for i, word in enumerate(words):
            if word[:1].lower() in ["a", "e", "i", "o", "u"]:
                words[i] = word + "ma" + ("a" * (i+1))
            else:
                words[i] = word[1:] + word[:1] + "ma" + ("a" * (i+1))

        return " ".join(words)
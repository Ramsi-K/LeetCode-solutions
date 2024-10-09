class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        n = 0
        for i, char in enumerate(word):
            if char == ch:
                stack.insert(0, char)
                n = i + 1
                break
            else:
                stack.insert(0, char)

        if n > 0:
            return "".join(stack) + word[n:]
        return word


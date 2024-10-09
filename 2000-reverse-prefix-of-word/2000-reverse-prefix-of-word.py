class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        n = 0
        for i in range(len(word)):
            if word[i] == ch:
                stack.insert(0, word[i])
                n = i + 1
                break
            else:
                stack.insert(0, word[i])

        if n > 0:
            return "".join(stack) + word[n:]
        return word


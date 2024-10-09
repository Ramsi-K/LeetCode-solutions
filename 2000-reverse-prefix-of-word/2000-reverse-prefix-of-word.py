class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        n = 0
        found = False
        for char in word:
            if char == ch:
                stack.insert(0, char)
                n += 1
                found = True
                break
            else:
                stack.insert(0, char)
                n += 1

        if found:
            return "".join(stack) + word[n:]
        return word


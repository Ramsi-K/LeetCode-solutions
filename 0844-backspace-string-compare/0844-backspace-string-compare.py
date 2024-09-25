class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        for i, char in enumerate(s):
            if char == "#":
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(char)
        # print(''.join(stack_s))

        for i, char in enumerate(t):
            if char == "#":
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(char)
        # print(''.join(stack_t))

        return stack_s == stack_t
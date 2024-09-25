class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_stack(string):
            stack = []
            for char in string:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return stack
        return build_stack(s) == build_stack(t)
   
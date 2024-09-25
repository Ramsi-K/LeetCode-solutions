class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # stack_s = []
        # stack_t = []
        # for char in s:
        #     if char == "#":
        #         if stack_s:
        #             stack_s.pop()
        #     else:
        #         stack_s.append(char)
        # # print(''.join(stack_s))

        # for char in t:
        #     if char == "#":
        #         if stack_t:
        #             stack_t.pop()
        #     else:
        #         stack_t.append(char)
        # print(''.join(stack_t))
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
        # return stack_s == stack_t
   
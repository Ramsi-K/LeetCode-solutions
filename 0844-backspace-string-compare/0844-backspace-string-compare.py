class Solution:
    # def backspaceCompare(self, s: str, t: str) -> bool:
    #     stack_s = []
    #     stack_t = []
    #     for i, char in enumerate(s):
    #         if char == "#":
    #             if stack_s:
    #                 stack_s.pop()
    #         else:
    #             stack_s.append(char)
    #     # print(''.join(stack_s))

    #     for i, char in enumerate(t):
    #         if char == "#":
    #             if stack_t:
    #                 stack_t.pop()
    #         else:
    #             stack_t.append(char)
    #     # print(''.join(stack_t))

    #     return stack_s == stack_t
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(string):
            skip = 0
            for char in reversed(string):
                if char == "#":
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield char

        return all(x == y for x, y in zip(process(s), process(t))) and len(list(process(s))) == len(list(process(t)))

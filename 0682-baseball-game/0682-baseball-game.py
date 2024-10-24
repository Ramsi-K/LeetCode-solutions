class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op.lstrip("-").isdigit():
                stack.append(int(op))
            elif op == "C" and stack:
                stack.pop()
            elif op == "D" and stack:
                stack.append(stack[-1] * 2)
            elif op == "+" and len(stack) > 1:
                stack.append(stack[-1] + stack[-2])

        return sum(stack)
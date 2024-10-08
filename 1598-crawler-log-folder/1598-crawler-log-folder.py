class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for action in logs:
            if stack and action == "../":
                stack.pop()
            elif action == "./" or action == "../":
                continue
            else:
                stack.append(action)
        
        # print(stack)
        # print(len(stack))
        return len(stack)


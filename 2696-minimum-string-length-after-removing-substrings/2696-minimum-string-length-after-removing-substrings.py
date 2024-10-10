class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if stack and stack[-1] + s[i] in ["AB", "CD"]:
                stack.pop()
                continue
            else:
                stack.append(s[i])
        
        # print(stack)
        return len(stack)
            
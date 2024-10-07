class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for char in s:
            # print(char.swapcase())
            if stack and stack[-1] == char.swapcase():
                stack.pop()
            
            else:
                stack.append(char)
        
        # print(stack)
        return "".join(stack)
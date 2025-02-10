class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        
        for ch in s:
            if ch.isdigit():
                if stack:  # Remove closest non-digit to the left
                    stack.pop()
            else:
                stack.append(ch)  # Add non-digit to stack
        
        return "".join(stack)
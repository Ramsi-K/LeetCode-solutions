class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        balance = 0
        start = 0
        
        for i, char in enumerate(s):
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            
            # When balance is 0, we have a complete primitive
            if balance == 0:
                # Append the current primitive without its outermost parentheses
                result.append(s[start + 1:i])  # Skip the first and last character
                start = i + 1  # Move to the next primitive start
        
        return ''.join(result)

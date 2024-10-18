class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_num = 0
        current_op = "+"
        n = len(s)

        for i in range(n):
            char = s[i]
            
            if char.isdigit():
                current_num = current_num * 10 + int(char)

            if char in "+-*/" or i == n - 1: 
                if current_op == "+":
                    stack.append(current_num)
                elif current_op == "-":
                    stack.append(-current_num)
                elif current_op == "*":
                    stack.append(stack.pop() * current_num)
                elif current_op == "/":
                    last_num = stack.pop()
                    if last_num < 0:
                        stack.append(int(last_num / current_num))  
                    else:
                        stack.append(last_num // current_num)  
                current_op = char
                current_num = 0

        # Sum all the numbers in the stack to get the final result
        return sum(stack)

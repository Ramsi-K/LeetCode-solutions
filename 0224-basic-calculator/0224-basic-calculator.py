class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        sign = 1 
        paren_stack = []  
        num = 0  

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)

            elif char == "+":
                result += sign * num
                num = 0  
                sign = 1  

            elif char == "-":
                result += sign * num
                num = 0  
                sign = -1  

            elif char == "(":
                paren_stack.append((result, sign))
                result, sign = 0, 1

            elif char == ")":
                result += sign * num
                num = 0  
                
                last_result, last_sign = paren_stack.pop()
                result = last_result + last_sign * result

        result += sign * num

        return result

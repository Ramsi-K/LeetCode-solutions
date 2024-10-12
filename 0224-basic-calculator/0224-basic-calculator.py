class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        sign = 1
        num_stack = []
        paren_stack = []

        for num in s:
            if num.isdigit():
                num_stack.append(num)

            elif num == "+" or num == "-":
                if num_stack:
                    result += int(''.join(num_stack)) * sign
                    num_stack.clear()  
                sign = 1 if num == "+" else -1

            elif num == "(":
                paren_stack.append((result, sign))
                result, sign = 0, 1

            elif num == ")":
                if num_stack:
                    result += int(''.join(num_stack)) * sign
                    num_stack.clear()
                    
                last_result, last_sign = paren_stack.pop()
                result = last_result + last_sign * result

            elif num == " ":
                continue

        if num_stack:
            result += int(''.join(num_stack)) * sign
        # print(result)
        return result
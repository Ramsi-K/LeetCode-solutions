class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # print(list(range(1, n+1)))
        out = []
        for i in range(1, n+1):
            # print(i)
            if i % 3 == 0:
                if i % 5 == 0: out.append("FizzBuzz")
                else: out.append("Fizz")
            elif i % 5 == 0: out.append("Buzz")
            else: out.append(str(i))
        # print(out)
        return out
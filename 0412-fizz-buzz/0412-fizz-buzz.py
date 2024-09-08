class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # print(list(range(1, n+1)))
        out = []
        for i in range(1, n+1):
            # print(i)
            if i % 15 == 0: out.append("FizzBuzz")
            elif i % 3 == 0: out.append("Fizz")
            elif i % 5 == 0: out.append("Buzz")
            else: out.append(str(i))
        # print(out)
        return out
class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        self.ans = []

        def solve(i):
            # base conditon - where recursion gets over
            if i > n:
                return

            cur = i  # 1 
            self.ans.append(cur)
            for i in range(10):
                tmp = str(cur) + str(i)  # 1 0 
                solve(int(tmp))

                # int tmp = cur*10 +  i;
                # solve(tmp,n);

        for i in range(1, 10):
            solve(i)

        return self.ans
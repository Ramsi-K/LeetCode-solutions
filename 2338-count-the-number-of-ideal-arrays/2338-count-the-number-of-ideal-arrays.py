class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7
        # Precompute factorials and inverse factorials
        max_n = n + 14  # For up to 14 length multiplicative chains (log2(10^4) ≈ 14)
        fact = [1] * (max_n)
        inv = [1] * (max_n)

        for i in range(1, max_n):
            fact[i] = fact[i-1] * i % MOD

        inv[max_n-1] = pow(fact[max_n-1], MOD - 2, MOD)
        for i in range(max_n - 2, 0, -1):
            inv[i] = inv[i+1] * (i+1) % MOD

        def comb_mod(n, k):
            if k < 0 or k > n:
                return 0
            return fact[n] * inv[k] % MOD * inv[n - k] % MOD

        # dp[length][value] = number of multiplicative chains of length `length` ending at `value`
        dp = [defaultdict(int) for _ in range(15)]
        for i in range(1, maxValue + 1):
            dp[1][i] = 1

        for l in range(2, 15):
            for v in range(1, maxValue + 1):
                for d in range(2*v, maxValue + 1, v):
                    dp[l][d] = (dp[l][d] + dp[l-1][v]) % MOD

        res = 0
        for l in range(1, 15):
            for v in dp[l]:
                ways = comb_mod(n - 1, l - 1)
                res = (res + dp[l][v] * ways) % MOD

        return res
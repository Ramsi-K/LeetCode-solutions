MOD = 10**9 + 7
MAX_N = 10**4 + 10       # Upper bound for maxValue
MAX_P = 15               # A number can have at most ~14 prime factors since 2^14 > 10^4

# Step 1: Sieve to compute smallest prime factor (SPF) for each number
sieve = [0] * MAX_N
for i in range(2, MAX_N):
    if sieve[i] == 0:
        for j in range(i, MAX_N, i):
            sieve[j] = i

# Step 2: Precompute prime factor exponent counts for every number
# ps[x] = list of exponents of prime factors in x (e.g. 12 → 2^2 * 3^1 → [2,1])
ps = [[] for _ in range(MAX_N)]
for i in range(2, MAX_N):
    x = i
    while x > 1:
        p = sieve[x]
        cnt = 0
        while x % p == 0:
            x //= p
            cnt += 1
        ps[i].append(cnt)

# Step 3: Precompute combinations C(n + e - 1, e) using Pascal’s Triangle
# Needed for multiset combinatorics (stars and bars)
c = [[0] * (MAX_P + 1) for _ in range(MAX_N + MAX_P)]
c[0][0] = 1
for i in range(1, MAX_N + MAX_P):
    c[i][0] = 1
    for j in range(1, min(i, MAX_P) + 1):
        c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % MOD

# Final solution class
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        ans = 0
        # For every number x from 1 to maxValue
        for x in range(1, maxValue + 1):
            mul = 1
            # For each prime exponent e in x's prime factorization
            for e in ps[x]:
                # Multiset combinations: ways to place e identical items into n positions
                # = C(n + e - 1, e)
                mul = mul * c[n + e - 1][e] % MOD
            ans = (ans + mul) % MOD
        return ans

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        def prime_score(x):
            score = 0
            for p in range(2, isqrt(x) + 1):
                if x % p == 0:
                    score += 1
                    while x % p == 0:
                        x //= p
            if x > 1:
                score += 1
            return score

        n = len(nums)
        scores = [prime_score(x) for x in nums]

        # Monotonic stack: count how many subarrays each nums[i] is max prime score in
        left = [0] * n
        right = [0] * n

        stack = []
        for i in range(n):
            while stack and scores[stack[-1]] < scores[i]:
                stack.pop()
            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)

        stack = []
        for i in reversed(range(n)):
            while stack and scores[stack[-1]] <= scores[i]:
                stack.pop()
            right[i] = stack[-1] - i if stack else n - i
            stack.append(i)

        count = [(nums[i], left[i] * right[i]) for i in range(n)]
        count.sort(reverse=True)

        res = 1
        for val, cnt in count:
            use = min(k, cnt)
            res = res * pow(val, use, MOD) % MOD
            k -= use
            if k == 0:
                break

        return res
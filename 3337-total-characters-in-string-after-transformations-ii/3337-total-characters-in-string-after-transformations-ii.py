from collections import Counter

MOD = 10**9 + 7

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        
        # Step 1: Count starting characters
        count = Counter(s)
        vec = [0] * 26
        for c in count:
            vec[ord(c) - ord('a')] = count[c]
        
        # Step 2: Build transformation matrix
        M = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for j in range(1, nums[i] + 1):
                M[i][(i + j) % 26] += 1
        
        # Step 3: Matrix exponentiation
        def mat_mult(A, B):
            res = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for k in range(26):
                    for j in range(26):
                        res[i][j] = (res[i][j] + A[i][k] * B[k][j]) % MOD
            return res

        def mat_pow(matrix, power):
            res = [[int(i == j) for j in range(26)] for i in range(26)]  # identity
            while power:
                if power % 2:
                    res = mat_mult(res, matrix)
                matrix = mat_mult(matrix, matrix)
                power //= 2
            return res

        M_t = mat_pow(M, t)

        # Step 4: Multiply vec × M^t
        final_vec = [0] * 26
        for j in range(26):
            for i in range(26):
                final_vec[j] = (final_vec[j] + vec[i] * M_t[i][j]) % MOD

        return sum(final_vec) % MOD

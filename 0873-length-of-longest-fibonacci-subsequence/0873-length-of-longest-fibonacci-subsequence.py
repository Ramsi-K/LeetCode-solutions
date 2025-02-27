class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        index_map = {x: i for i, x in enumerate(arr)}

        # dp[i][j] = length of the longest Fibonacci-like subsequence ending with (arr[i], arr[j])
        dp = [[2] * n for _ in range(n)]
        max_len = 0

        for j in range(n):
            for i in range(j):
                needed = arr[j] - arr[i]
                if needed in index_map:
                    k = index_map[needed]
                    if k < i:
                        dp[i][j] = dp[k][i] + 1
                    else:
                        # start a new sequence with (arr[i], arr[j])
                        dp[i][j] = 2
                else:
                    # if needed is not in the array, best we can do is 2 for (arr[i], arr[j])
                    dp[i][j] = 2

                max_len = max(max_len, dp[i][j])

        return max_len if max_len >= 3 else 0
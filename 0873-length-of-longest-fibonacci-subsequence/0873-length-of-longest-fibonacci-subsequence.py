class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        index_map = {x: i for i, x in enumerate(arr)}
        
        # dp[j] will be a dictionary:
        # dp[j][i] = length of Fibonacci-like sequence ending with arr[i] and arr[j]
        dp = [dict() for _ in range(n)]
        max_len = 0

        for j in range(n):
            for i in range(j):
                needed = arr[j] - arr[i]
                if needed in index_map:
                    k = index_map[needed]
                    if k < i:
                        # If we already have a chain ending at (k, i)
                        curr_len = dp[i].get(k, 2) + 1
                        dp[j][i] = curr_len
                        max_len = max(max_len, curr_len)
                    else:
                        # k >= i, not valid; store length=2
                        dp[j][i] = 2
                else:
                    # no predecessor => length=2 for the pair (arr[i], arr[j])
                    dp[j][i] = 2

        return max_len if max_len >= 3 else 0
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def canPartition(s: str, target: int) -> bool:
            # dp[i] is a set of possible sums that can be achieved using s[0:i]
            N = len(s)
            dp = [set() for _ in range(N + 1)]
            dp[0].add(0)
            
            # Build dp table: for each starting index i, try all possible splits ending at j
            for i in range(N):
                # Only proceed if there's at least one sum accumulated at dp[i]
                if dp[i]:
                    for j in range(i + 1, N + 1):
                        part = int(s[i:j])
                        for prev_sum in dp[i]:
                            dp[j].add(prev_sum + part)
            
            return target in dp[N]
        
        punishment = 0
        # Check each i in [1, n]
        for i in range(1, n + 1):
            s = str(i * i)
            if canPartition(s, i):
                punishment += i * i
        
        return punishment


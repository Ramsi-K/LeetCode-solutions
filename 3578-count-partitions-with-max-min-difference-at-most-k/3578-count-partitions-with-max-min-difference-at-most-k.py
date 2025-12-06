class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = pow(10, 9) + 7
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            largest = smallest = nums[i]
            for j in range(i, -1, -1):
                largest = max(largest, nums[j])
                smallest = min(smallest, nums[j])
                if largest - smallest > k:
                    break
                dp[i] += dp[j - 1] if j > 0 else 1
                dp[i] %= mod
        return dp[-1]

    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = pow(10, 9) + 7
        n = len(nums)
        dp = [1] + [0] * n
        largest = deque()
        smallest = deque()
        acc = 1
        j = 0
        for i in range(n):
            while largest and nums[largest[-1]] < nums[i]:
                largest.pop()
            largest.append(i)
            while smallest and nums[smallest[-1]] > nums[i]:
                smallest.pop()
            smallest.append(i)

            while nums[largest[0]] - nums[smallest[0]] > k:
                acc = (acc - dp[j]) % mod
                j += 1
                if largest[0] < j:
                    largest.popleft()
                if smallest[0] < j:
                    smallest.popleft()
            dp[i + 1] = acc
            acc = (acc + dp[i + 1]) % mod
        return dp[-1]

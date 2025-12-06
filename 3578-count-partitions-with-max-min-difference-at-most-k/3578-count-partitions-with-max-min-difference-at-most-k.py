class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = pow(10,9)+7
        n = len(nums)
        dp = [1]+[0]*n
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

            while nums[largest[0]]-nums[smallest[0]] > k:
                acc = (acc-dp[j]) % mod
                j += 1
                if largest[0] < j:
                    largest.popleft()
                if smallest[0] < j:
                    smallest.popleft()
            dp[i+1] = acc
            acc = (acc+dp[i+1]) % mod
        return dp[-1]

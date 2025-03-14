class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        best = total//k
        worst = 1
        while best > worst:
            mid = (best + worst) //2
            value = sum([x%mid for x in candies])
            if total - value < k*mid:
                best = mid
            else:
                worst = mid+1
        if worst == 1:
            return best
        if worst == total//k and total - sum([x%worst for x in candies]) >= k*worst:
            return worst
        return worst-1
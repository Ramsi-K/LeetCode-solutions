class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones = list(stones)
        jewels = list(jewels)
        count = 0
        for i in stones:
            if i in jewels: count += 1
        
        return count
        # return sum(1 for i in stones if i in jewels)
from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        total = count1 + count2
        
        if any(v % 2 != 0 for v in total.values()):
            return -1

        diff = {}
        for k in total:
            d = count1[k] - total[k] // 2
            if d != 0:
                diff[k] = abs(d)

        to_swap = []
        for k, v in diff.items():
            to_swap.extend([k] * (v // 1))

        to_swap.sort()
        global_min = min(basket1 + basket2)

        cost = 0
        for i in range(len(to_swap) // 2):
            cost += min(to_swap[i], 2 * global_min)

        return cost

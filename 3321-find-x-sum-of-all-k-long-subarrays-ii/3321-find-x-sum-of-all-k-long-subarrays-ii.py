from collections import defaultdict
import heapq

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        counts = defaultdict(int)

        # Init freq for first window
        for i in range(k):
            counts[nums[i]] += 1

        low = []          # max-heap (neg counts, neg nums)
        high = []         # min-heap (top x)
        high_nums = set() # current top-x nums
        value = 0         # current x-sum

        # Fill heaps
        for n, c in counts.items():
            heapq.heappush(low, (-c, -n))

        # Move top-x to high
        while len(high_nums) < x and low:
            c, n = heapq.heappop(low)
            heapq.heappush(high, (-c, -n))
            high_nums.add(-n)
            value += c * n  # since both neg, adds (+)

        res.append(value)

        # Helper: update a number's heap entry
        def process_num(num):
            if num in high_nums:
                heapq.heappush(high, (counts[num], num))
            else:
                heapq.heappush(low, (-counts[num], -num))

        # Clean invalid items (lazy deletion)
        def clean_low():
            while low and (counts[-low[0][1]] != -low[0][0] or -low[0][1] in high_nums):
                heapq.heappop(low)
        def clean_high():
            while high and (counts[high[0][1]] != high[0][0] or high[0][1] not in high_nums):
                heapq.heappop(high)

        # Slide window
        for i in range(k, len(nums)):
            old = nums[i - k]
            new = nums[i]
            if old == new:
                res.append(value)
                continue

            counts[old] -= 1
            counts[new] += 1

            # Adjust running sum
            if old in high_nums:
                value -= old
            if new in high_nums:
                value += new

            # Update heaps
            process_num(old)
            process_num(new)
            clean_low()
            clean_high()

            # Swap if ordering breaks
            if low and high:
                if -low[0][0] > high[0][0] or (-low[0][0] == high[0][0] and -low[0][1] > high[0][1]):
                    nc, nn = heapq.heappop(low)
                    oc, on = heapq.heappop(high)
                    high_nums.remove(on)
                    high_nums.add(-nn)
                    value -= on * counts[on]
                    value += (-nn) * counts[-nn]
                    heapq.heappush(high, (-nc, -nn))
                    heapq.heappush(low, (-oc, -on))

            # Refill top-x
            clean_low()
            while low and len(high_nums) < x:
                nc, nn = heapq.heappop(low)
                value += (-nn) * counts[-nn]
                heapq.heappush(high, (-nc, -nn))
                high_nums.add(-nn)

            res.append(value)

        return res

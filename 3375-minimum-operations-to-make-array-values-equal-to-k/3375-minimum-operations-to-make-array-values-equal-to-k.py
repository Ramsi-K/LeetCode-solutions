class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # If any number is less than k, it's impossible
        if any(num < k for num in nums):
            return -1

        # Count frequency of each number
        count = Counter(nums)

        # Only care about values > k
        vals = sorted(set(nums), reverse=True)
        ops = 0

        while vals and vals[0] > k:
            max_val = vals[0]
            # All values greater than the next smaller value must be equal
            # So we find the next smaller value h to collapse to
            for i in range(1, len(vals)):
                h = vals[i]
                higher_vals = vals[:i]  # all vals > h
                if len(set(higher_vals)) == 1:
                    ops += 1
                    # simulate the collapse to h
                    count[h] += sum(count[v] for v in higher_vals)
                    for v in higher_vals:
                        del count[v]
                    vals = sorted(count.keys(), reverse=True)
                    break
            else:
                # If we couldn't find a valid h, check if we can collapse everything directly to k
                if len(set(v for v in vals if v > k)) == 1:
                    ops += 1
                    return ops
                return -1

        return ops if set(count.keys()) == {k} else -1
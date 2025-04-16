class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        def countAtMost(k):
            count = 0
            left = 0
            freq = defaultdict(int)
            pair_count = 0

            for right in range(len(nums)):
                pair_count += freq[nums[right]]
                freq[nums[right]] += 1

                while pair_count >= k:
                    freq[nums[left]] -= 1
                    pair_count -= freq[nums[left]]
                    left += 1

                count += right - left + 1
            return count

        total = len(nums) * (len(nums) + 1) // 2
        return total - countAtMost(k)
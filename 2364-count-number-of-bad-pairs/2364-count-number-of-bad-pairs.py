class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        diff_counts = Counter(i - nums[i] for i in range(n))  # Count occurrences of (i - nums[i])
        good_pairs = sum(count * (count - 1) // 2 for count in diff_counts.values())  # Compute good pairs
        total_pairs = (n * (n - 1)) // 2  # Total possible pairs
        return total_pairs - good_pairs  # Bad pairs = Total - Good
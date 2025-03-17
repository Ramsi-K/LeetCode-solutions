class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)  # Count occurrences of each number
        return all(count % 2 == 0 for count in freq.values()) 
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        all_binaries = {format(i, f'0{n}b') for i in range(2**n)}
        given = set(nums)
        # The difference will be the set of binary strings that are not in nums.
        diff = all_binaries - given
        return diff.pop()  # Return any one string from the difference.
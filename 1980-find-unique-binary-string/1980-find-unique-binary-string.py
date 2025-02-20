class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        result = []
        for i in range(n):
            # Flip the i-th character of the i-th string:
            if nums[i][i] == '0':
                result.append('1')
            else:
                result.append('0')
        return ''.join(result)
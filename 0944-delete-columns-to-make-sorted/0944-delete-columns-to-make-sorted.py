class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        out = 0
        num_columns = len(strs[0])

        # Loop through each column
        for col in range(num_columns):
            for row in range(1, len(strs)):
                if strs[row][col] < strs[row - 1][col]:
                    out += 1
                    break
        return out
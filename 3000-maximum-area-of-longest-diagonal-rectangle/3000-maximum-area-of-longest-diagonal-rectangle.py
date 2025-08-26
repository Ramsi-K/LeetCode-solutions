from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = -1
        max_area = -1

        for l, w in dimensions:
            diag_sq = l * l + w * w  # squared diagonal
            area = l * w

            # Check if this rectangle has a longer diagonal
            if diag_sq > max_diag:
                max_diag = diag_sq
                max_area = area
            # If diagonal is equal, pick the one with larger area
            elif diag_sq == max_diag and area > max_area:
                max_area = area

        return max_area

        
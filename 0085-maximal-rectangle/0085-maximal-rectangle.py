class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        cols = len(matrix[0])
        # h stores the heights of bars for the current row (plus a 0 sentinel)
        h = [0] * (cols + 1)
        max_area = 0

        for row in matrix:
            # Update heights for the current row
            for j in range(cols):
                h[j] = h[j] + 1 if row[j] == '1' else 0
            
            # Monotonic Stack to find the largest rectangle in the current histogram
            stack = [-1]
            for i in range(cols + 1):
                # While current height is lower than the height at the stack's top
                while stack[-1] != -1 and h[i] < h[stack[-1]]:
                    height = h[stack.pop()]
                    width = i - stack[-1] - 1
                    area = height * width
                    if area > max_area:
                        max_area = area
                stack.append(i)
                
        return max_area
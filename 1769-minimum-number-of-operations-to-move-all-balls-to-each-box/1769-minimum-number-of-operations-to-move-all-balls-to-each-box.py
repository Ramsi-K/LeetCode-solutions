class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n

        # Precompute cumulative sums of indices weighted by the presence of balls
        total_left = 0
        total_right = 0
        weight_left = 0
        weight_right = 0

        # Calculate total weight and distances for the right side
        for i in range(n):
            if boxes[i] == '1':
                weight_right += 1
                total_right += i

        # Compute the answer for each box
        for i in range(n):
            # Add contributions from the left and right
            answer[i] = total_left + total_right

            # Update totals for the next box
            if boxes[i] == '1':
                weight_left += 1
                weight_right -= 1

            total_left += weight_left
            total_right -= weight_right

        return answer

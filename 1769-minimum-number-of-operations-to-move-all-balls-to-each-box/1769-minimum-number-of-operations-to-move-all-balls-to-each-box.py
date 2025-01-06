class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n

        # Precompute the total weights and costs for the right side
        right_weight = sum(int(box) for box in boxes)
        right_cost = sum(i * int(box) for i, box in enumerate(boxes))

        left_weight = 0
        left_cost = 0

        for i in range(n):
            # Current box operations = left + right
            answer[i] = left_cost + right_cost

            # Update left and right contributions
            if boxes[i] == '1':
                left_weight += 1
                right_weight -= 1

            left_cost += left_weight
            right_cost -= right_weight

        return answer
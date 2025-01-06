class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        
        # Precompute positions of all balls
        ball_positions = [i for i, char in enumerate(boxes) if char == '1']
        
        # Calculate the total moves for each box
        for i in range(n):
            answer[i] = sum(abs(i - pos) for pos in ball_positions)
        
        return answer
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        
        for i in range(n):
            # Multiply the binary values with their respective distances
            answer[i] = sum((abs(i - j) * int(boxes[j]) for j in range(n)))
        
        return answer